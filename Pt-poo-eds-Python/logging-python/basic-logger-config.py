
import logging
import math

# Format for log messages
LOG_FORMAT = "%(Levelname)s %(asctime)s - %(message)s "
# Create and configure logger
logging.basicConfig( filename = "E:\\python\\Lumberjack.log",
                    level =  logging.DEBUG,
                    format = LOG_FORMAT,
                    filemode="w" )
# By default the file mode it is configured in append()

# can configure a name, by default at at below
logger = logging.getLogger()

# Test the logger
logger.info("Our first message.")
logger.debug("Debuging log")
logger.warning("Warning log")
logger.error("Error log")
logger.critical("Critical")

# Assign a level
# print(logger.level)

# Aplying to cuadritic formula
def quadratic_formula(a, b ,c):
    """ Return the solution to equation ax^2+bx+c """
    logger.info( "quadratic_formula({0},{1},{2})".format(a,b,c) )
    
    # Compute the discriminant
    logger.debug("#Compute the discriminant")
    disc = b**2 - 4*a*c
    
    # Compute the two roots
    logger.debug("#Compute the two roots")
    root1 = ( -b + math.sqrt(disc)/( 2*a ) )
    root2 = ( -b - math.sqrt(disc)/( 2*a ) )
    
    # Return the roots
    logger.debug("Return the roots")
    return( root1, root2 )

roots = quadratic_formula(1,0,-4)
# Create a problem
roots = quadratic_formula(1,0,1)
print(roots)