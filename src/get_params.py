#!/usr/bin/env python
#
# Author: Kenton Murray [kenton (at) jhu (dot) edu] 
# Created: 7/18/22
#

import argparse
import yaml


def get_fairseq_params(inputfile):
  inference_params = {}
  with open(inputfile) as f:
    for line in f:
      if line.startswith("Namespace("):
        line = line.lstrip("Namespace(")
        line = line.rstrip(")\n")
        params = line.split(",")
        for param in params:
          k,v = param.split("=")
          k = k.lstrip("\' ")
          k = k.rstrip("\'")
          v = v.lstrip("\' ")
          v = v.rstrip("\'")
          if k not in inference_params:
            inference_params[k] = v
          else:
            print("DANGER WILL ROBINSON!") #TODO
  inference ={}
  inference["inference"] = inference_params
  return inference

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-t', '--toolkit', required=True, type=str, help="Please specify which MT toolkit your parameters are from")
  parser.add_argument('-i', '--inputfile', required=True, type=str)
  parser.add_argument('-o', '--outputfile', default="data.yaml", type=str)
  args = parser.parse_args()

  if args.toolkit == "fairseq":
    inference = get_fairseq_params(args.inputfile)

  with open(args.outputfile, 'w') as outfile:
      yaml.dump(inference, outfile, default_flow_style=False)

if __name__ == '__main__':
    main()
