const kue = require('kue');
const queue = kue.createQueue();

const jobData = {
    phoneNumber: 'string',
    message: 'string',
};

let job = queue
    .create('push_notification_code', jobData)
    .save((err) => {
        if (!err) {
            console.log(`Notification job created: ${job.id}`)
        }
    })
    .on('complete', () => console.log('Notification job completed'))
    .on('failed', () => console.log('Notification job failed'));
