from queue import PriorityQueue


def best_first_search(problem, f):
    initial = problem.initial
    frontier = PriorityQueue()
    frontier.put((f(initial), initial))
    reached = {initial.key: initial}
    while(not is_empty(frontier)):
        node = frontier.get()
        if problem.is_goal(node.state):
            return node
        for child in expand(problem, node):
            state = child.state
            if (not state in reached) or (child.path_cost < reached[state].path_cost):
                reached[state] = child
                frontier.put(f(child), child)
    return None


def expand(problem, node):
    state = node.state
    nodes = []
    for action in problem.actions(state):
        new_state = problem.result(state, action)
        cost = node.path_cost + problem.action_cost(state, action, new_state)
        nodes.append(Node(state=new_state, parent=node, action=action, path_cost = cost))
    return nodes

