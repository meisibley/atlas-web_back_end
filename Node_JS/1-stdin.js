//display input message
process.stdout.write('Welcome to Holberton School, what is your name?\n');
process.stdin
    .on('readable', () => {
        //sets up an event listener for the readable event
        const name = process.stdin.read();
        //read data from the standard input
        if (name !== null) {
            process.stdout.write(`Your name is: ${name}`);
            //display user inputted message
        }
    })
    .on('end', () => {
        process.stdout.write('This important software is now closing\n');
        //sets up an event listener for the end event on the standard input
        //stream. This event fires when the user signals the end of input
        //(e.g., pressing Ctrl+D)
    });