#!/usr/bin/env python
#
#
# Copyright (C) 2013 Cisco Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#vlan 2001
# vn-segment 22001
# exit
#int nve 1
# member vni 22001
#    ingress-replication protocol static
#      peer-ip 2.2.2.2
#end
#
#show nve vni ingress-replication 22001

import re
import sys
from cli import *
from xml.dom import minidom


cli('configure terminal ;vlan '+ sys.argv[1] +' ;vn-segment '+ sys.argv[2])
cli('configure terminal ;interface nve1 ;member vni '+ sys.argv[2] +' ;ingress-replication protocol static ;peer-ip 2.2.2.2')

r = cli('show nve vni ingress-replication ' + sys.argv[2]); print r
