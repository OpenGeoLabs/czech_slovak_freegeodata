#!/usr/bin/env python3

import sys
import argparse
import configparser
import os

try:
    from graphviz import Digraph
except ImportError:
    sys.stderr.write("Python bindings for Graphviz are not available. See https://github.com/xflr6/graphviz.\n")


parser = argparse.ArgumentParser(prog="graph_generate",
                                 description="This utility creates graph from transformations defined in crs_trans.ini configuration file.")
parser.add_argument("--region", "-r",
                    help="Region filter. When specified, only transformations for defined region will be included in output.")
parser.add_argument("--trans_conf", "-t",
                    help="Path to crs_trans.ini file.",
                    default="crs_trans.ini")
parser.add_argument("--label", "-l",
                    help="Output graph label.")
parser.add_argument("output",
                    help="Output PDF file base name (no extension should be defined).")

args = parser.parse_args()

"""
This part loads transformations.
"""
transfs = []
if not os.path.isfile(args.trans_conf):
    sys.stderr.write("Specified transformation configuration file \"{}\" does not exists.\n".format(args.trans_conf))
    sys.exit(1)

transConfig = configparser.ConfigParser()
try:
    transConfig.read(args.trans_conf)
except Exception:
    sys.stderr.write("Unable to open transformations configuration file {}.\n".format(args.trans_conf))
    sys.exit(1)

for transSection in transConfig:
    if transSection != "DEFAULT":
        transformation = {}
        transSectionContent = transConfig[transSection]
        transformation["bidir"] = False

        try:
            transformation["key"] = transSection
            transformation["from"] = transSectionContent.get("CrsFrom")
            transformation["to"] = transSectionContent.get("CrsTo")
            regions = transSectionContent.get("Regions", None)
            if isinstance(regions, str) and regions is not None:
                regions = regions.split(" ")
        except Exception:
            sys.stderr.write("Unable to process transformation {}.\n".format(transSection))
            continue

        # finding oposite direction tronsformation
        opositeFound = False
        for definedTrans in transfs:
            if definedTrans["from"] == transformation["to"] and \
               definedTrans["to"] == transformation["from"] and \
               definedTrans["bidir"] == False:
                definedTrans["bidir"] = True
                opositeFound = True
                break

        if not opositeFound and (args.region is None or (args.region is not None and args.region in regions)):
            transfs.append(transformation)

"""
This part generates graph.
"""

dot = Digraph(name=args.output,
              engine="neato",
              format="png")
dot.attr(overlap="false")
dot.attr(label=args.label)
dot.attr(labelloc="top")
dot.attr(fontsize="20")

for trans in transfs:
    dot.node(trans["from"].replace(":", "_"),
             label=trans["from"],
             fillcolor="#A7C3F3",
             style="filled")

    dot.node(trans["to"].replace(":", "_"),
             label = trans["to"],
             fillcolor="#A7C3F3",
             style="filled")

    dot.edge(trans["from"].replace(":", "_"),
             trans["to"].replace(":", "_"),
             color="#5F5F5F",
             dir="none" if trans["bidir"] else "forward")

dot.render()
