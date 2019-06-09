var express = require('express');
var app = express();
var mysql = require('mysql');

/** MySQL */
var sqlconn = mysql.createConnection({
  host : 'lookvies.c4gfbjjoxspj.us-east-2.rds.amazonaws.com',
  user : 'lookvie',
  password : 'lookvie1234',
  database : 'lookvie'
});
sqlconn.connect();

app.get('/', function (req, res) {
  res.send('This is LookVie Home page!');
});

app.post('/get_timetable', function(req, res) {
    var sql = 'SELECT * FROM timetable';
    var result = ['cinema', 'movie', 'screen', 'time'];
    result['cinema'] = [];
    result['movie'] = [];
    result['screen'] = [];
    result['time'] = [];
    sqlconn.query(sql, function(err, rows, fields) {
        if(err) {
            console.log(err);
            res.send('');
        } else {
            for(var i = 0; i < rows.length; i++)
            {
                result['cinema'].push(rows[i].cinema);
                result['movie'].push(rows[i].movie);
                result['screen'].push(rows[i].screen);
                result['time'].push(rows);
            }
            //console.log(result);
            res.json({
                cinema: result['cinema'][0],
                movie: result['movie'][0],
                screen: result['screen'][0],
                time: result['time'][0]
            });
        }
    });
});

app.listen(3000, function () {
  console.log('Connected!');
});