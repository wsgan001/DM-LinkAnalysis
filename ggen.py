
if __name__ == "__main__":
    import argparse
    import sys
    parser = argparse.ArgumentParser()

    parser.add_argument('-v',
                        default=0,
                        type=int,
                        dest='VERTEX',
                        help='Set number of vertices.')
    parser.add_argument('-e',
                        default=0,
                        type=int,
                        dest='EDGE',
                        help='Set number of edges')
    parser.add_argument('-o',
                        default='graph_gen.txt',
                        dest='OUTPUT',
                        help='Place the output into <file>')

    args = parser.parse_args()

    vertex  = args.VERTEX
    edge    = args.EDGE
    outfile = args.OUTPUT

    if vertex <= 0 or edge <= 0:
        print('Please set number of vertices and edges.')
        sys.exit()

    max_edge = vertex ** 2
    edge     = min(edge, max_edge)
    import numpy as np

    choice = np.sort(np.random.choice(max_edge, edge, replace=False))

    with open(outfile, 'w') as f:
        for i in choice:
            f.write(str(i // vertex + 1) + ',' + str(i % vertex + 1) + '\n')
