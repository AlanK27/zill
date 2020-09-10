
const db = require('../util/db/mysql_db')

module.exports = class Db {
  constructor(data) {
    this.data = data;
  }

  static fetchA(df, ofset, amnt) {
    return db.execute(`select * from ${df} limit ${ofset},${amnt};`);
  }

  static db_size(df) {
    return db.execute(`select count(*) from ${df}`)
  }
}
