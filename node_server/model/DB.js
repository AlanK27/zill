
const db = require('../util/db/mysql_db')


module.exports = class Db {
  constructor(data) {
    this.data = data;
  }

  static fetchA(df, ofset, amnt) {
    return db.execute(`
    select * 
    from ${df}
    order by date desc
    limit ${ofset},${amnt};`);
  }

  static fetchAll(df) {
    return db.execute(`
    select * 
    from ${df}
    order by date desc;`);
  }

  static fetchQ(df, ofset, amnt) {
    return db.execute(`
    select * 
    from ${df}
    order by address, date desc
    limit ${ofset},${amnt};`);
  }

  static fetchQAll(df) {
    return db.execute(`
    select * 
    from ${df}
    order by address, date desc;`);
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
    from ${df} 
    where address rlike ?
    order by date desc
    limit ${ofset}, ${amnt}
    ;`, [addr]
    )
  }

  static insert(file, table) {
    return db.query(`
    insert into ${table} 
    (date, address, location, price, beds, baths, sqft, per_sqft) 
    values ?;
    `,  file, (err, res) => {
          console.log(err|| res)
        }
    )
  }
};
