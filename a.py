const mysql = require('mysql');
const { sqlConfig } = require('../config.js');

class Database {
    constructor() {
        this.db = mysql.createConnection(sqlConfig);
    }

    async getPosts(order) {
        return new Promise(async (resolve, reject) => {
            let stmt = `SELECT * FROM posts ORDER BY ${ order }`;
            this.db.query(stmt, (err, result) => {
                if(err)
                    reject(err);
                resolve(result);
            })

        });
    }
}

module.exports = Database;
