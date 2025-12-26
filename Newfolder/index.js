const express = require("express");
const app = express();
app.use(express.json());

// Parse form data
app.use(express.urlencoded({ extended: true }));
// Mock database of students (for demo purposes)
const students = [
  {
    id: 101,
    name: "Alice",
    email: "alice@example.com",
    password: "123456", // in real apps, use hashed passwords
    section: "A",
    branch: "Science",
    school: "Sunrise High School"
  },
  {
    id: 102,
    name: "Bob",
    email: "bob@example.com",
    password: "abcdef",
    section: "B",
    branch: "Commerce",
    school: "Sunrise High School"
  }
];
app.get("/", (req, res) => {
  res.send("Server is running 🚀");
});
app.get("/index", (req, res) => {
  res.redirect(indexe.html);
});
app.post("/signup", (req, res) => {
  const { name, email, password } = req.body;

  if (!name || !email || !password) {
    return res.status(400).json({ status: false, message: "All fields required" });
  }

  // Find student by email (you could also use name)
  const student = students.find(
    (s) => s.email === email && s.password === password
  );

  if (!student) {
    return res.status(401).json({ status: false, message: "Invalid credentials" });
  }

  // If found, return student details
  res.json({
    status: true,
    message: "Signup success",
    data: {
      name: student.name,
      section: student.section,
      branch: student.branch,
      school: student.school
    }
  });
});

app.listen(3000, () => console.log("API running on port 3000"));
