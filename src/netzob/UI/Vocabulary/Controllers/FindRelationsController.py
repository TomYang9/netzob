# -*- coding: utf-8 -*-

#+---------------------------------------------------------------------------+
#|          01001110 01100101 01110100 01111010 01101111 01100010            |
#|                                                                           |
#|               Netzob : Inferring communication protocols                  |
#+---------------------------------------------------------------------------+
#| Copyright (C) 2011 Georges Bossert and Frédéric Guihéry                   |
#| This program is free software: you can redistribute it and/or modify      |
#| it under the terms of the GNU General Public License as published by      |
#| the Free Software Foundation, either version 3 of the License, or         |
#| (at your option) any later version.                                       |
#|                                                                           |
#| This program is distributed in the hope that it will be useful,           |
#| but WITHOUT ANY WARRANTY; without even the implied warranty of            |
#| MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the              |
#| GNU General Public License for more details.                              |
#|                                                                           |
#| You should have received a copy of the GNU General Public License         |
#| along with this program. If not, see <http://www.gnu.org/licenses/>.      |
#+---------------------------------------------------------------------------+
#| @url      : http://www.netzob.org                                         |
#| @contact  : contact@netzob.org                                            |
#| @sponsors : Amossys, http://www.amossys.fr                                |
#|             Supélec, http://www.rennes.supelec.fr/ren/rd/cidre/           |
#+---------------------------------------------------------------------------+

#+----------------------------------------------
#| Global Imports
#+----------------------------------------------
from gettext import gettext as _
import logging

#+----------------------------------------------
#| Local Imports
#+----------------------------------------------
from netzob.Inference.Vocabulary.RelationFinder import RelationFinder


#+----------------------------------------------
#| FindRelationsController:
#+----------------------------------------------
class FindRelationsController(object):

    #+----------------------------------------------
    #| Constructor:
    #| @param netzob: the netzob main class
    #+----------------------------------------------
    def __init__(self, netzob):
        # create logger with the given configuration
        self.log = logging.getLogger(__name__ + '.py')
        self.netzob = netzob

    #+----------------------------------------------
    #| Called when user wants to find the potential relations
    #+----------------------------------------------
    def buildRelations(self, symbols):
        finder = RelationFinder(self.netzob.getCurrentProject())
        finder.execute(symbols[0])
