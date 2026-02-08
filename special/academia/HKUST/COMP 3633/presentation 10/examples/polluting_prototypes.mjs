import bodyParser from "body-parser";
import express from "express";

const app = express();

app.get(
  "/", // Whenever we GET /, ...
  (_req, res) => {
    res.send("Hello, world!"); // Return `Hello, world!`.
  },
);

// Simplified from UTCTF 2024/Easy Mergers: https://ctftime.org/writeup/39045
const secret = {}; // Need to make this have `cmd`

function isObject(obj) {
  return typeof obj === "function" || typeof obj === "object"; // Remember that function is a subtype of object.
}

// curl -i -X POST "http://localhost/merge" -H "Content-Type: application/json" --data-raw '{"attributes": ["__proto__"], "values": [{"cmd": "cat flag.txt"}]}'
app.post(
  "/merge", // Whenever we POST /merge, ...
  bodyParser.json(),
  (req, res) => {
    const data = req.body;
    if ("attributes" in data && "values" in data) {
      const orig = {};
      for (
        let k = 0;
        k < Math.min(data.attributes.length, data.values.length);
        ++k
      ) {
        if (
          !(orig[data.attributes[k]] === undefined) &&
          isObject(orig[data.attributes[k]]) &&
          isObject(data.values[k])
        ) {
          for (const key in data.values[k]) {
            orig[data.attributes[k]][key] = data.values[k][key]; // Vulnerable
          }
        } else if (
          !(orig[data.attributes[k]] === undefined) &&
          Array.isArray(orig[data.attributes[k]]) &&
          Array.isArray(data.values[k])
        ) {
          orig[data.attributes[k]] = orig[data.attributes[k]].concat(
            data.values[k],
          ); // Could be vulnerable
        } else {
          orig[data.attributes[k]] = data.values[k]; // Could be vulnerable
        }
      }
    }
    res.send(
      secret.cmd === "cat flag.txt"
        ? "flag{:blobcat_radiation:}"
        : "Try harder",
    );
  },
);

// Start a server on http://localhost:80
app.listen(80, () => console.log("Listening on port 80"));
