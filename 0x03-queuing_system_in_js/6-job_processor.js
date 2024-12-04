import kue from 'kue';

const queue = kue.createQueue();

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;

  sendNotification(phoneNumber, message);

  done();
});

queue.on('ready', () => {
  console.log('Queue is ready and processing jobs...');
});

queue.on('error', (err) => {
  console.log('Error in processing the job:', err);
});

