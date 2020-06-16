# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class mysql_connection(models.Model):
    _name = "connect.mysql"
    _description = 'Connect to mysql'
    server_name = fields.Char('Server', required=True, help="The server name, could be an IP or a URL")
    database_name = fields.Char('Database name', required=True)
    user_name = fields.Char('User name', required=True)
    password = fields.Char('Password', required=True)
    query = fields.Text('SQL Query/Instruction', required=True,
                        help="A Select statement or an insert/update/delete instruction")
    result = fields.Text('Result')

    @api.multi
    def mysql_connect(self,name):
        try:
            import mysql.connector

            myconn = mysql.connector.connect(
                host=self.server_name,
                user=self.user_name,
                passwd=self.password ,
                database = self.database_name,

            )

            mycursor = myconn.cursor()
            mycursor.execute(self.query)
            if self.query.strip().split(" ")[0].lower() == "select":
                rows = mycursor.fetchall()
                my_result = ""
                for i in rows:
                    for x in i:
                        my_result += "\t" + str(x)
                    my_result += "\n"

                # Show the result
                self.result = my_result
            else:
                mycursor.commit()
                self.result = "Statement executed successfully, please check your database or make a select statement."
            mycursor.close()
        except:
            self.result = "An Error Occurred, please check your parameters!\n" \
                          "And make sure (mysql) is installed (pip3 install mysql)."
