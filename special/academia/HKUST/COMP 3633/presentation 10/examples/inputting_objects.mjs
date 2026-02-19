import bodyParser from "body-parser";
import express from "express";

const app = express();

app.get(
  "/", // Whenever we GET /, ...
  (_req, res) => {
    res.send("Hello, world!"); // Return `Hello, world!`.
  },
);

// curl -i -X GET "http://localhost/query?key=value&nested[key]=value&__proto__=test&test[__proto__]=test" -g
app.get(
  "/query", // Whenever we GET /query, ...
  (req, res) => {
    res.json({
      query: req.query,
      prototype: String(Object.getPrototypeOf(req.query)),
    });
  },
);

// curl -i -X POST "http://localhost/body-parser/json" -H "Content-Type: application/json" --data-raw '{"key": "value", "nested": {"key": "value"}, "__proto__": "test", "test": {"__proto__": ["test"]}}'
app.post(
  "/body-parser/json", // Whenever we POST /body-parser/json, ...
  bodyParser.json(), // Check if `Content-Type` is `application/json` and parses the body if so, otherwise does not.
  (req, res) => {
    res.json({
      body: req.body,
      prototype: String(Object.getPrototypeOf(req.body)),
    });
  },
);

// curl -i -X POST "http://localhost/body-parser/urlencoded" -H "Content-Type: application/x-www-form-urlencoded" -d "key=value" -d "nested[key]=value" -d "__proto__=test" -d "test[__proto__]=test"
app.post(
  "/body-parser/urlencoded", // Whenever we POST /body-parser/urlencoded
  bodyParser.urlencoded({
    extended: true, // Note that `extended` is by default `true`, but this is deprecated and might change in the future.
  }),
  (req, res) => {
    res.json({
      body: req.body,
      prototype: String(Object.getPrototypeOf(req.body)),
    });
  },
);

// curl -i -X POST "http://localhost/body-parser/urlencoded/unextended" -H "Content-Type: application/x-www-form-urlencoded" -d "key=value" -d "nested[key]=value" -d "__proto__=test" -d "test[__proto__]=test"
app.post(
  "/body-parser/urlencoded/unextended", // Whenever we POST /body-parser/urlencoded-unextended
  bodyParser.urlencoded({
    extended: false, // `false` makes nested objects not work.
  }),
  (req, res) => {
    res.json({
      body: req.body,
      prototype: String(Object.getPrototypeOf(req.body)),
    });
  },
);

// Start a server on http://localhost:80
app.listen(80, () => console.log("Listening on port 80"));
