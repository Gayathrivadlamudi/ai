const express = require("express");
const path = require("path");

const app = express();
const PORT = 4000;

//🔹 MIDDLEWARE 1: parse form data
app.use(express.urlencoded({ extended: true }));
app.use(express.static("public"));
// 🔹 MIDDLEWARE 2: custom middleware
app.use((req, res, next) => {
  console.log("👉 Middleware is running");
  console.log("Request URL:", req.url);
  next(); // VERY IMPORTANT
});
app.use((req, res, next) => {
  console.log("👉 Middleware the second is running");
  console.log("Request URL:", req.url);
  next(); // VERY IMPORTANT
});

// 🔹 Serve HTML file
app.get("/hi", (req, res) => {
  res.redirect( "/indexMiddle.html");
});
// 🔹 Handle form submit
app.post("/login",(req, res) => {
  console.log("👉 Route handler reached");
  console.log("Form data:", req.body);
  res.send("Login successful! Check terminal.");
});
app.listen(4000, () => {
  console.log(`Server middle running on http://localhost:${PORT}`);
});
