const http = require("http");
const port = 3000;
let x;
let y;
let depth;
let mag;

const express = require('express');

const app = express();

app.get('', (req, res) => {
  res.setHeader("Access-Control-Allow-Origin", "*");
  x = req.query.x
  y = req.query.y
  depth = req.query.depth
  mag = req.query.mag
  console.log(x, y, depth, mag)
  const childProcess = require('child_process');
  // command = ["python3", "./web/python/predict_eq_myfcn2.py", "-m", "./web/python/model_13", "-x", str(X), "-y", str(Y), "-depth", str(Depth), "-mag", str(Mag)]
  childProcess.execSync('python3 python/predict_eq_myfcn2.py -m python/model_13 -x ' + x + ' -y ' + y + ' -depth ' + depth + ' -mag ' + mag, (error, stdout, stderr) => {
    if (error) return console.error('ERROR', error);
  });

  const fs = require("fs");
  let header = x + "+" + y + "+" + depth + "+" + mag + ",";
  // header for check
  fs.readFile("python/predicted_data.csv", "utf-8", (err, data) => {
    res.end(header + data);
  });
});

app.listen('3000', () => {
  console.log('Application started');
});