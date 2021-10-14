const spawn = require("child_process").spawn;
const args = process.argv.slice(2)
const pythonProcess = spawn('python3', ["tess.py", args[0]]);

pythonProcess.stdout.on('data', (data) => {
    process.stdout.write(data)
});


