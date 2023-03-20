import { instance } from './index'

function getWeeklyNotification () {
  return instance.get('/api/notification/weekly/')
}

export {
  getWeeklyNotification,
};
