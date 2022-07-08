"""
-Select all sales of new vehicles and output them to the screen in a 
comma-delimited format
-Output a comma-delimited list of all salespeople with their gross sales 
and save it to a file that can be imported to a spreadsheet

1. Connect to the database.
2. Construct a query for new vehicles or gross sales.
3. Issue the query.
4. Format the results into a comma-delimited string.
5. Output the data to a file or e-mail.

"""

import sqlite3

class QueryTemplate:
    def connect(self):
        self.conn = sqlite3.connect("sales.db")
    
    def construct_query(self):
        raise NotImplementedError()

    def do_query(self):
        results = self.conn.execute(self.query)
        self.results = results.fetchall()

    def format_results(self):
        output = []
        for row in self.results:
            row = [ str(i) for i in row ]
            output.append( ", ".join(row) )
        self.format_results = "\n".join( output )

    def output_results(self):
        raise NotImplementedError()

import datetime

class NewVehiclesQuery(QueryTemplate):
    def construct_query(self):
        # return super().construct_query()
        self.query = "select * from Sales where new='true'"
        
    def output_results(self):
        print( self.formatted_results )

class UserGrossQuery( QueryTemplate ):
    def construct_query(self): 
        self.query = ("select salesperson, sum(amt) "+ 
                      "from sales group by salesperson" )
        
    def output_results(self):
        filename = "gross_sales{0}".format(
            datetime.date.today().stfrtime("%Y%m%d")
        )
        with open( filename,'w') as outfile:
            outfile.write( self.formatted_results )

# 
# class QueryTemplate:
#     def connect(self):
#         pass
    
#     def construct_query( self ):
#         pass

#     def do_query( self ):
#         pass
    
#     def format_results(self ):
#         pass
    
#     def output_results( self ):
#         pass
    
#     def process_format(self):
#         self.connect()
#         self.construct_query()
#         self.do_query()
#         self.format_results()
#         self.output_results() 
    