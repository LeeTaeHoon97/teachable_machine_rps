let { PythonShell } = require('python-shell')

PythonShell.run('run.py', null, (err, data) => {
    if (err) throw err;

    console.log(data);
});
