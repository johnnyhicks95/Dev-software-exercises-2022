import re
import sys
import json
from pathlib import Path

""" the directives are:
• include: Copy the contents of another file here
• variable: Insert the contents of a variable here
• loopover: Repeat the contents of the loop for a variable that is a list
• endloop: Signal the end of looped text
• loopvar: Insert a single value from the list being looped over
 """

DIRECTIVE_RE = re.compile(
    r'/\*\*\s*(include|variable|loopover|endloop|loopvar)'
    r'\s*([^ *]*)\s*\*\*/'
)

class TemplateEngine:
    def __init__( self, infilename, outfilename, contextfilename ):
        self.template = open(infilename).read()
        self.working_dir = Path(infilename).absolute().parent
        self.pos = 0
        self.outfile = open( outfilename, 'w' )
        with open( contextfilename ) as contextfile:
            self.context = json.load(contextfile)

    """ def process(self):
        print("PROCESSING ...") """

    # replacing position advancing line
    def process(self):
        match = DIRECTIVE_RE.search(self.template, pos=self.pos)
        while match:
            self.outfile.write( self.template[self.pos:match.start()] )
            directive, argument = match.groups()
            method_name = 'process_{}'.format(directive)
            getattr( self, method_name )( match, argument )
            match = DIRECTIVE_RE.search(self.template, pos = self.pos)
        self.outfile.write(self.template[self.pos:])
        
    def process_include( self, match, argument ):
        with( self.working_dir/argument ).open() as includefile:
            self.outfile.write(includefile.read())
            self.pos = match.end()
    
    def process_variable( self, match, argument ):
        self.outfile.write( self.context.get(argument, '') )
        self.pos = match.end
        
    def procces_loopover(self, match, argument):
        self.loop_index=0
        self.loop_list = self.context.get( argument, [] )
        self.pos = self.loop_pos = match.end()
        
    def procces_loopvar( self, match, argument ):
        self.outfile.write( self.loop_list[self.loop_index] )
        self.pos = match.end()

    def process_endloop( self, match, argument ):
        self.loop += 1
        if self.loop_index >= len( self.loop_list ):
            self.pos = match.end()
            del self.loop_index
            del self.loop_list
            del self.loop_pos
        else:
            self.pos = self.loop_pos

if __name__ == '__main__':
    infilename, outfilename, contextfilename = sys.argv[1:]
    engine = TemplateEngine( infilename, outfilename, contextfilename )
    engine.process()


""" <html>
 <body>
<h1>This is the title of the front page</h1>
<a href="link1.html">First Link</a>
<a href="link2.html">Second Link</a>
<p>My name is Dusty.
This is the content of my front page. It goes below the menu.</p>
<table>
<tr><th>Favourite Books</th></tr>
<tr><td>Thief Of Time</td></tr>
<tr><td>The Thief</td></tr>
<tr><td>Snow Crash</td></tr>
<tr><td>Lathe Of Heaven</td></tr>
</table>
 </body>
</html>
 """
