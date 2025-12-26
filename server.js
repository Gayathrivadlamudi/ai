const express = require("express");
const path = require("path");

const app = express();

// Middleware
app.use(express.urlencoded({ extended: true }));
app.use(express.static("public"));

// Mock database
const students = [
  {
    name: "Alice",
    email: "alice@example.com",
    password: "123456"
  },
  {
    name: "Bob",
    email: "bob@example.com",
    password: "abcdef"
  }
];
// Home page
app.get("/", (req, res) => {
  res.redirect("/index.html");
});
// Signup/Login route
app.post("/signup", (req, res) => {
  const { email, password } = req.body;

  const student = students.find(
    s => s.email === email && s.password === password
  );

  if (!student) {
    return res.redirect("/index.html?error=1");
  }

  res.redirect(`/welcome.html?name=${student.name}&email=${student.email}`);
});

app.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});
