#!/usr/bin/bash
diff <(objdump -d breadth.v1) <(objdump -d breadth.v2)
