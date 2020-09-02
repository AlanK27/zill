
const db = require('../util/db/mysql_db')

module.exports = class Db {
  constructor(data) {
    this.data = data;
  }

  static fetchAll() {
    return db.execute('select * from testbase.main limit 5;');
  }
}







