class RouteTrieNode:
    def __init__(self):
        self.children={}
        self.handler=None
        # Initialize the node with children as before, plus a handler

    def insert(self,page):
        self.children[page]=RouteTrieNode()
        # Insert the node as before

        # The Router class will wrap the Trie and handle
class Router:
    def __init__(self,root_handler,not_handler):
        self.root=RouteTrieNode()
        self.root_handler=root_handler
        self.not_handler=not_handler
            # Create a new RouteTrie for holding our routes
            # You could also add a handler for 404 page not found responses as well!

    def add_handler(self, path,handler):
        path=self.split_path(path)
        cur=self.root
        for page in path:
            if page not in cur.children:
                cur.insert(page)
            cur=cur.children[page]
        cur.handler=handler


            # Add a handler for a path
            # You will need to split the path and pass the pass parts
            # as a list to the RouteTrie

    def lookup(self,path):
        if path == "/":
            return self.root_handler

        path_list = self.split_path(path)

        current_node = self.root

        for page in path_list:

            try:
                if current_node.children[page]:
                    current_node = current_node.children[page]
            except:
                return self.not_handler
        if not current_node.handler:
            return self.not_handler

        return current_node.handler
            # lookup path (by parts) and return the associated handler
            # you can return None if it's not found or
            # return the "not found" handler if you added one
            # bonus points if a path works with and without a trailing slash
            # e.g. /about and /about/ both return the /about handler

    def split_path(self, path):
        try:
            if path[0]=='/':
                path=path[1:]
            if path[-1]=='/':
                path=path[:-1]
        except:
            return path
        path=path[1::].split('/')
        return path
        # you need to split the path into parts for
        # both the add_handler and lookup functions,
        # so it should be placed in a function here


        # Here are some test cases and expected outputs you can use to test your implementation

        # create the router and add a route
router = Router("root handler",'not found handler')  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

        # some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler'
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one


router2 = Router("root handler",'not found handler')
print(router2.lookup(""))#it should print not found handler

router3 = Router("root handler",'not found handler')
router3.add_handler("/blog/2019-01-15/my-awesome-blog-post", "blog handler")  # add a route

        # some lookups with the expected output
print(router3.lookup("/"))  # should print not found handler
print(router3.lookup("/home"))  # should print 'not found handler'
print(router3.lookup("/blog/2019-01-15/"))  # should print not found handler
print(router3.lookup("/blog/2019-01-15/my-awesome-blog-post"))  # should print blog handler



