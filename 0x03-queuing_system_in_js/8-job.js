import kue from 'kue';

function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((jobData) => {
    const job = queue.create('push_notification_code_3', jobData)
      .save((err) => {
        if (err) {
          console.log('Job creation failed:', err);
        } else {
          console.log(`Notification job created: ${job.id}`);
        }
      });

    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    job.on('failed', (errorMessage) => {
      console.log(`Notification job ${job.id} failed: ${errorMessage}`);
    });

    job.on('progress', (percentage) => {
      console.log(`Notification job ${job.id} ${percentage}% complete`);
    });
  });
}

export default createPushNotificationsJobs;
