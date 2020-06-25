const py = module.exports;
const fs = require("fs");
const _ = require("lodash");

py.process = ({ spec, operations, models, handlebars }) => {
  py.spec = spec;
  const templates = [];

  // Check for response resolution
  operations.forEach((op) => {
    const responseModel = getModelByName(op.responseModel, models);
    if (responseModel && responseModel.requiresResolution) {
      op.responseModelRequiresResolution = true;
    }
  });

  templates.push({
    src: "generated-client.py.hbs",
    dest: "okta/generated-client.py",
    context: { operations, spec },
  });

  handlebars.registerHelper({
    operationArgumentBuilder,
    pyDocstringBuilder,
    updatePath,
    displayMethodName,
    multilineURL,
  });

  handlebars.registerPartial(
    "partials.copyrightHeader",
    fs.readFileSync("openapi/templates/partials/copyrightHeader.hbs", "utf8")
  );

  // fs.writeFile(
  //   "openapi/createdFiles.json",
  //   JSON.stringify(templates),
  //   function (error) {
  //     console.log(error);
  //   }
  // );

  return templates;
};

// Helper functions
function getModelByName(name, models) {
  if (name == undefined) {
    return null;
  }
  const found = models.filter((model) => {
    return model.modelName === name;
  });
  return found[0] || null;
}

function isPostOrPut(method) {
  return method === "post" || method === "put";
}

// Handlebars helpers
function operationArgumentBuilder(operation) {
  let args = [];
  operation.pathParams.map((param) => args.push(param.name));

  // check body model if required with request
  if (operation.bodyModel && isPostOrPut(operation.method)) {
    let bodyModel = _.snakeCase(operation.bodyModel);
    args.push(bodyModel);
  }

  if (operation.queryParams.length) {
    args.push("query_params");
  }
  return (args.length ? " ".repeat(12) : "") + args.join(", ");
}

function pyDocstringBuilder(method) {
  const docs = [];

  const ONE_TAB = " ".repeat(12);
  const TWO_TABS = ONE_TAB + " ".repeat(4);

  let descString = method.description || `Method for\n${method.path}`;
  descString.match(/.{1,55}/g).forEach((line) => {
    docs.push(`${ONE_TAB}${line.trim()}`);
  });

  docs.push(`${ONE_TAB}Args:`);
  if (method.pathParams.length) {
    method.pathParams
      .map((param) => {
        return `${TWO_TABS}${_.snakeCase(param.name)} {str}`;
      })
      .forEach((doc) => docs.push(doc));
  }

  if (!method.isArray && method.bodyModel) {
    docs.push(`${TWO_TABS}{${_.snakeCase(method.bodyModel)}}`);
  }

  if (method.queryParams.length) {
    docs.push(
      `${TWO_TABS}query_params {dict}: Map of query parameters for request`
    );
    method.queryParams
      .map((param) => {
        return `${TWO_TABS}[query_params.${param.name}] {str}`;
      })
      .forEach((queryParam) => docs.push(queryParam));
  }

  if (method.responseModel) {
    docs.push(`${ONE_TAB}Returns:`);
    if (method.isArray) {
      docs.push(
        `${TWO_TABS}list: Collection of ${method.responseModel} instances.`
      );
    } else {
      docs.push(`${TWO_TABS}${method.responseModel}`);
    }
  }

  return docs.join("\n");
}

function updatePath(operation) {
  let result = operation.path;
  if (operation.pathParams.length) {
    operation.pathParams.forEach((param) => {
      result = result.replace(param, { param });
    });
    result = multilineURL(result);
  }
  return result;
}

function multilineURL(path) {
  let pieces = path.split("/").filter((segment) => {
    return segment.length > 0;
  });
  let result = [];
  let current = "";
  const LIMIT = 50;

  pieces.forEach((piece) => {
    if (piece.length + current.length <= LIMIT) {
      current = current.concat(`/${piece}`);
    } else {
      result.push(current);
      current = piece;
    }
  });

  result.push(current);
  return result.join(`\n${" ".repeat(16)}`);
}

function hasPathParams(operation) {
  return operation.pathParams.length ? "f" : "";
}

function displayMethodName(name) {
  const LONG_WORDS = {
    application: "app",
    administrator: "admin",
  };
  if (name.length > 60) {
    for (let key in LONG_WORDS) {
      name = name.replace(key, LONG_WORDS[key]);
    }
  }

  return name;
}
