import bodyParser from "body-parser";
import express from "express";
import flat from "flat";
import { compile } from "pug";

const app = express();

app.get(
  "/", // Whenever we GET /, ...
  (_req, res) => {
    res.send("Hello, world!"); // Return `Hello, world!`.
  },
);

// Modified from Cyber Apocalypse 2021/BlitzProp: https://ctftime.org/writeup/39045
globalThis.flag = "flag{you_should_know_this_song_or_else_...}";
const authors = {};

// No answer here! hehe
app.post(
  "/song", // Whenever we POST /song, ...
  bodyParser.json(),
  (req, res) => {
    for (const key of Object.keys(req.body)) {
      if (key.startsWith("__proto__")) delete req.body[key]; // No naughty allowed!!!
    }
    const { song } = flat.unflatten(req.body);
    if (song === "FIRE BIRD")
      return res.send(
        compile("span by #{author}")({
          author: authors["FIRE BIRD"] ?? "Roselia",
        }),
      );
    return res.send("Please provide us with the name of an existing song");
  },
);

// Start a server on http://localhost:80
app.listen(80, () => console.log("Listening on port 80"));
