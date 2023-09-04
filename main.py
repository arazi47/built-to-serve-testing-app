# Import views is needed even though it's not used
# so that route() decorators get called
import views
from ws2g.main import run

run()