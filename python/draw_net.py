#!/usr/bin/env python
"""
Draw a graph of the net architecture.
"""
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from google.protobuf import text_format

import caffe
import caffe.draw
from caffe.proto import caffe_pb2


def parse_args():
    """Parse input arguments
    """

    parser = ArgumentParser(description=__doc__,
                            formatter_class=ArgumentDefaultsHelpFormatter)

    parser.add_argument('input_net_proto_file',
                        help='Input network prototxt file')
    parser.add_argument('output_image_file',
                        help='Output image file')
    parser.add_argument('--rankdir',
                        help=('One of TB (top-bottom, i.e., vertical), '
                              'RL (right-left, i.e., horizontal), or another '
                              'valid dot option; see '
                              'http://www.graphviz.org/doc/info/'
                              'attrs.html#k:rankdir'),
                        default='LR')
    parser.add_argument('--margin',
                        help=('Margin parameter'),
                        default='')
    parser.add_argument('--page',
                        help=('Page parameter'),
                        default='')
    parser.add_argument('--pagesize',
                        help=('Pagesize parameter'),
                        default='')
    parser.add_argument('--size',
                        help=('Size parameter'),
                        default='')

    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    net = caffe_pb2.NetParameter()
    text_format.Merge(open(args.input_net_proto_file).read(), net)
    print('Drawing net to %s' % args.output_image_file)
    caffe.draw.draw_net_to_file(net, args.output_image_file, args.rankdir,
             args.margin, args.page, args.pagesize, args.size)


if __name__ == '__main__':
    main()
