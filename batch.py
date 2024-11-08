import random
import utils
import sys
import argparse

DEFAULT_INI_STATE = "125340687"
DEFAULT_MAX_DEPTH = 30

##### MODIFICAR [4] #####
ALGORITHMS = ('BFS', 'DFS_Graph', 'DFS_Backtracking', 'PI_Backtracking',
              'Greedy_Manhattan', 'A_Manhattan',
              'A_Euclidean', 'IDA_Manhattan', 'A_Natdescolocadas', 'A_Natsecuencia')
##### ------------- #####

def random_state():
    def gen_state():
        return "".join(list(map(lambda a: str(a), random.sample(range(9), 9))))
    state = gen_state()
    while not utils.isSolvable(state):
        state = gen_state()
    return state


def many_random_states(n):
    for i in range(n):
        yield random_state()


def batch_run(states,
              algorithms,
              max_depth=DEFAULT_MAX_DEPTH,
              print_info="all"):

    ##### MODIFICAR [5] #####
    stats = {alg: {'generated': 0, 'expanded': 0, 'max_stored': 0, 'sol_cost': 0,
                   'max_depth': 0, 'runtime': 0.0, 'count': 0} for alg in algorithms}
    
    ##### ------------- #####

    if print_info in {"all", "raw"}:
        print("# {:8s} {:20s} {:>10s} {:>10s} {:>10s} {:>10s} {:>10s} {:>12s}".format("state", "strategy", "generated", "expanded", "max_stored", 
                                                                           "sol_cost", "max_depth", "time(s)"))
        print("#")
    
    for state in states:

        if not(utils.validateState(state)):
            sys.stderr.write(f"\n[WW] State '{state}' is not valid. Please check format. Skipping...\n\n") 
            continue

        if not(utils.isSolvable(state)):
            sys.stderr.write(f"\n[WW] State '{state}' is not solvable. Skipping...\n\n") 
            continue

        for algorithm in algorithms:

            ##### MODIFICAR [6] #####

            if str(algorithm) == 'BFS':
                utils.graphSearch(state, utils.function_1, utils.function_0)
                path, sol_cost, expanded, depth, runtime, generated, max_stored, memory_rep = \
                          utils.graphf_path, utils.graphf_cost, utils.graphf_counter, \
                          utils.graphf_depth, utils.time_graphf, utils.node_counter, \
                          utils.max_counter, utils.max_rev_counter
   
            elif str(algorithm) == 'DFS_Graph':
                utils.graphSearch(state, utils.function_N, utils.function_0, max_depth)
                path, sol_cost, expanded, depth, runtime, generated, max_stored, memory_rep = \
                          utils.graphf_path, utils.graphf_cost, utils.graphf_counter, \
                          utils.graphf_depth, utils.time_graphf, utils.node_counter, \
                          utils.max_counter, utils.max_rev_counter
    
            elif str(algorithm) == 'DFS_Backtracking':
                utils.DFS_B(state, max_depth)
                path, sol_cost, expanded, depth, runtime, generated, max_stored = \
                          utils.graphf_path, utils.graphf_cost, utils.graphf_counter, \
                          utils.graphf_depth, utils.time_graphf, utils.node_counter, \
                          utils.max_node_stored
    
            elif str(algorithm) == 'PI_Backtracking':
                utils.ID_B(state)
                path, sol_cost, expanded, depth, runtime, generated, max_stored = \
                          utils.graphf_path, utils.graphf_cost, utils.graphf_counter, \
                          utils.graphf_depth, utils.time_graphf, utils.node_counter, \
                          utils.max_node_stored
    
            elif str(algorithm) == 'Greedy_Manhattan':
                utils.graphSearch(state, utils.function_0, utils.getManhattanDistance)
                path, sol_cost, expanded, depth, runtime, generated, max_stored, memory_rep = \
                          utils.graphf_path, utils.graphf_cost, utils.graphf_counter, \
                          utils.graphf_depth, utils.time_graphf, utils.node_counter, \
                          utils.max_counter, utils.max_rev_counter
    
            elif str(algorithm) == 'A_Manhattan':
                utils.graphSearch(state, utils.function_1, utils.getManhattanDistance)
                path, sol_cost, expanded, depth, runtime, generated, max_stored, memory_rep = \
                          utils.graphf_path, utils.graphf_cost, utils.graphf_counter, \
                          utils.graphf_depth, utils.time_graphf, utils.node_counter, \
                          utils.max_counter, utils.max_rev_counter
    
            elif str(algorithm) == 'A_Euclidean':
                utils.graphSearch(state, utils.function_1, utils.getEuclideanDistance)
                path, sol_cost, expanded, depth, runtime, generated, max_stored, memory_rep = \
                          utils.graphf_path, utils.graphf_cost, utils.graphf_counter, \
                          utils.graphf_depth, utils.time_graphf, utils.node_counter, \
                          utils.max_counter, utils.max_rev_counter
    
            elif str(algorithm) == 'IDA_Manhattan':
                utils.IDA_B(state, utils.getManhattanDistance)
                path, sol_cost, expanded, depth, runtime, generated, max_stored = \
                          utils.graphf_path, utils.graphf_cost, utils.graphf_counter, \
                          utils.graphf_depth, utils.time_graphf, utils.node_counter, \
                          utils.max_node_stored
                          
            elif str(algorithm) == 'A_Natdescolocadas':
                utils.IDA_B(state, utils.descolocadas)
                path, sol_cost, expanded, depth, runtime, generated, max_stored = \
                        utils.graphf_path, utils.graphf_cost, utils.graphf_counter, \
                        utils.graphf_depth, utils.time_graphf, utils.node_counter, \
                        utils.max_node_stored
        
            elif str(algorithm) == 'A_Natsecuencia':
                utils.IDA_B(state, utils.secuencia)
                path, sol_cost, expanded, depth, runtime, generated, max_stored = \
                        utils.graphf_path, utils.graphf_cost, utils.graphf_counter, \
                        utils.graphf_depth, utils.time_graphf, utils.node_counter, \
                        utils.max_node_stored
    
            depth = int(depth) 
            
            # Acumulación de estadísticas en stats
            stats[algorithm]['generated'] += generated
            stats[algorithm]['expanded'] += expanded
            stats[algorithm]['max_stored'] += max_stored
            stats[algorithm]['sol_cost'] += sol_cost
            stats[algorithm]['max_depth'] += depth
            stats[algorithm]['runtime'] += runtime
            stats[algorithm]['count'] += 1  # Incrementa el contador de ejecuciones para el promedio
    
            if print_info in {"all", "raw"}:
                print(f"""{state:10s} {algorithm:20s} {generated:10d} {expanded:10d} {max_stored:10d} {sol_cost:10d} {depth:10d} {runtime:12.6f}""")

        if print_info in {"all", "raw"}:
            print("#")

    if print_info in {"all", "stats"}:
        ##### MODIFICAR [7] #####
        print("# strategy            generated   expanded max_stored       cost  max_depth      time(s)")
        for algorithm, data in stats.items():
            if data['count'] > 0:  # Evita división por cero
                avg_generated = data['generated'] / data['count']
                avg_expanded = data['expanded'] / data['count']
                avg_max_stored = data['max_stored'] / data['count']
                avg_sol_cost = data['sol_cost'] / data['count']
                avg_max_depth = data['max_depth'] / data['count']
                avg_runtime = data['runtime'] / data['count']  # Asegúrate de que la clave es 'runtime'
                        
                # Imprimir las estadísticas promedio en el formato requerido
                print(f"{algorithm:20s} {avg_generated:10.1f} {avg_expanded:10.1f} {avg_max_stored:10.1f} "
                      f"{avg_sol_cost:10.1f} {avg_max_depth:10.1f} {avg_runtime:12.6f}")
        ##### ------------- #####


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
                description='8-puzzle batch solver. \
                             By default, solves the initial state "{}" \
                             using all available algorithms.'.format(DEFAULT_INI_STATE))
    parser.add_argument('-s', '--states', nargs='+', metavar="STATE", 
                         default=[DEFAULT_INI_STATE],
                         help='Provide a list of initial states. Default: "{}"'.format(DEFAULT_INI_STATE))
    parser.add_argument('-r', '--random-states', metavar="N", nargs='?', 
                         type=int, const=10, default=0, 
                         help="Use %(metavar)s randomly generated initial states. Default: %(const)d.")
    parser.add_argument('--random-seed', metavar="INT", default=None,
                         help="Set random seed initializer (to ensure reproducibility).")
    parser.add_argument('-l', '--list-algorithms', action='store_true', 
                         default=False, help="Show list of all search algorithms available.")
    parser.add_argument('-a', '--algorithms', nargs='+', choices=ALGORITHMS, default=ALGORITHMS, metavar="ALG",
                         help="Set search algorithms to be used. Default: all.")
    parser.add_argument('-d', '--max-depth', type=int, default=DEFAULT_MAX_DEPTH,
                         help="Maximum search depth (when applicable). Default: %(default)s.")
    parser.add_argument('-p', '--print-info', choices=("raw", "stats", "all"), default="all",
                         help="Set which information to print. Default: %(default)s.")

    args = parser.parse_args()

    
    if args.list_algorithms:
        sys.stderr.write("List of available search algorithms:\n")
        for a in ALGORITHMS:
            sys.stderr.write(f"* {a}\n")
        sys.exit(0)

    if args.random_states:
        if args.random_seed:
            random.seed(args.random_seed)
        batch_run(many_random_states(args.random_states), 
                  args.algorithms, 
                  max_depth=args.max_depth,
                  print_info=args.print_info)

    else:
        batch_run(args.states, 
                  args.algorithms, 
                  max_depth=args.max_depth,
                  print_info=args.print_info)
