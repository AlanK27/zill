
const db = require('../util/db/mysql_db')

module.exports = class Db {
  constructor(data) {
    this.data = data;
  }

  static fetchA(df, ofset, amnt) {
    return db.execute(`
    select * 
    from ${df}
    order by address 
    limit ${ofset},${amnt};`);
  }

  static db_size(df) {
    return db.execute(`
    select count(*) 
    from ${df};`)
  }

  static db_search_size(df, addr) {
    return db.execute(`
    select count(*) 
    from (${df})
    where address rlike ?
    ;`, [addr]
    )
  }

  static search(df, addr, ofset, amnt) {
    return db.execute(`
    select * 
    from main 
    where address rlike ?
    order by date desc
    limit ${ofset}, ${amnt}
    ;`, [addr]
    )
  }

}
