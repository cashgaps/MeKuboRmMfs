#-----------------------------------------------------------------------
# Name:    MeKuboRmMfs
# Purpose:    MeKuboRmMfs
#
# Author:    me
#
# Created:    2024052018300101
# Copyright:    (c) me 2024052018300101
# Licence:    copyright & all rights reserved
#-----------------------------------------------------------------------
#_____________________________________________________________________
#
import atexit
import json
import math
import os
import pathlib
import random
import shutil
import signal
import socket
import stat
import subprocess
import sys
import threading
import time
import tkinter \
    .filedialog
import traceback
#
#
import colorama
import pyperclip
import segno
#
#_____________________________________________________________________
#_____________________________________________________________________
try \
:
    colorama \
    .just_fix_windows_console \
    (
    )
except \
:
    pass
#_____________________________________________________________________
#_____________________________________________________________________
try \
:
    if \
        pyperclip \
        .paste \
        (
        ) \
            != \
            '' \
    :
        pyperclip \
        .copy \
        (
            pyperclip \
            .paste \
            (
            ) \
        )
except \
:
    pyperclip \
    .copy \
    (
        '' \
    )
#_____________________________________________________________________
#_____________________________________________________________________
MeCounter0 \
    = \
    0
###timestamper0
##global \
##    MeCounter0
##MeCounter0 \
##    += \
##    1
##if \
##    (
##        MeCounter0 \
##            >= \
##            10000 \
##    ) \
##:
##    MeCounter0 \
##        = \
##        0
##TimeStamper \
##    = \
##    lambda \
##    : \
##    (
##        (
##            int \
##            (
##                time \
##                .time \
##                (
##                )
##            ) \
##            * \
##            (
##                10 \
##                ** \
##                4
##            )
##        ) \
##        + \
##        (
##            MeCounter0 \
##        ) \
##    )
###timestamper1
MeToggle0 \
    = \
    0
MeTimeStamper \
    = \
    None
MeSep0 \
    = \
    '    '
MeSep1 \
    = \
    '_'
MeCounter1 \
    = \
    0
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeExceptor \
    (
    ) \
:
    print \
    (
        '\n' \
        + \
        '\n' \
        + \
        ':' \
        + \
        '\n' \
            ,
    )
    traceback \
    .print_exc \
    (
        file \
            = \
            sys \
            .stdout \
    )
    print \
    (
        '\n' \
        + \
        ':' \
        + \
        '\n' \
        + \
        '\n' \
            ,
    )
#_____________________________________________________________________
#_____________________________________________________________________
try \
:
    atexit \
    .register \
    (
        MeExceptor \
            ,
    )
except \
:
    pass
try \
:
    signal \
    .signal \
    (
        signal \
        .SIGINT \
            ,
        MeExceptor \
            ,
    )
except \
:
    pass
try \
:
    signal \
    .signal \
    (
        signal \
        .SIGTERM \
            ,
        MeExceptor \
            ,
    )
except \
:
    pass
try \
:
    signal \
    .signal \
    (
        signal \
        .SIGBREAK \
            ,
        MeExceptor \
            ,
    )
except \
:
    pass
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeHaveTxtFile \
    (
    ) \
:
    with \
        open \
        (
            os \
            .path \
            .join \
            (
                '.' \
                    ,
                'zoo' \
                    ,
                '2paths.ini' \
                    ,
            ) \
                ,
            mode \
                = \
                'rb' \
                ,
        ) \
    as \
        FileObject1 \
    :
        global \
            MeTwoPaths0
        MeTwoPaths0 \
            = \
            FileObject1 \
            .readline \
            (
            ) \
            .decode \
            (
                'ascii' \
                    ,
            ) \
            .strip \
            (
            )
        global \
            MeTwoPaths1
        MeTwoPaths1 \
            = \
            FileObject1 \
            .readline \
            (
            ) \
            .decode \
            (
                'ascii' \
                    ,
            ) \
            .strip \
            (
            )
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeKuboFilesLs \
    (
        Thing \
            = \
            None \
            ,
    ) \
:
    MePopenProcess00env0 \
        = \
        dict \
        (
        )
    MePopenProcess00env0 \
    .update \
    (
        os \
        .environ \
    )
    MePopenProcess00env0 \
    .update \
    (
        {
            'IPFS_PATH' \
            : \
                os \
                .path \
                .join \
                (
                    MeTwoPaths1 \
                        ,
                )
                    ,
        }
    )
    MeCheckOutputProcess00args0 \
        = \
        ' ' \
        .join \
        (
            [
                os \
                .path \
                .join \
                (
                    MeTwoPaths0 \
                        ,
                ) \
                    ,
                'files' \
                    ,
                'ls' \
                    ,
                '--' \
                    ,
            ] \
                ,
        )
    MeCheckOutputProcess00 \
        = \
        subprocess \
        .check_output \
        (
            MeCheckOutputProcess00args0 \
                ,
            cwd \
                = \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                )
                ,
            env \
                = \
                MePopenProcess00env0 \
                ,
            universal_newlines \
                = \
                False \
                ,
            shell \
                = \
                True \
                ,
        )
    for \
        y \
    in \
        [
            x
                for \
                    x \
                in \
                    MeCheckOutputProcess00 \
                    .decode \
                    (
                        'ascii' \
                            ,
                    ) \
                    .split \
                    (
                        '\n' \
                            ,
                    )
                    if \
                        x \
                            != \
                            '' \
        ] \
    :
        try \
        :
            MeKuboFilesRm \
            (
                y \
                    ,
            )
        except \
        :
            pass
    MeKuboRepoGc \
    (
    )
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeKuboFilesRm \
    (
        Thing \
            = \
            None \
            ,
    ) \
:
    MePopenProcess00env0 \
        = \
        dict \
        (
        )
    MePopenProcess00env0 \
    .update \
    (
        os \
        .environ \
    )
    MePopenProcess00env0 \
    .update \
    (
        {
            'IPFS_PATH' \
            : \
                os \
                .path \
                .join \
                (
                    MeTwoPaths1 \
                        ,
                )
                    ,
        }
    )
    MeCheckOutputProcess00args0 \
        = \
        ' ' \
        .join \
        (
            [
                os \
                .path \
                .join \
                (
                    MeTwoPaths0 \
                        ,
                ) \
                    ,
                'files' \
                    ,
                'rm' \
                    ,
                '--force' \
                    ,
                '--' \
                    ,
                '/' \
                + \
                Thing \
                    ,
            ] \
                ,
        )
    MeCheckOutputProcess00 \
        = \
        subprocess \
        .check_output \
        (
            MeCheckOutputProcess00args0 \
                ,
            cwd \
                = \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                )
                ,
            env \
                = \
                MePopenProcess00env0 \
                ,
            universal_newlines \
                = \
                False \
                ,
            shell \
                = \
                True \
                ,
        )
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeKuboRepoGc \
    (
        Thing \
            = \
            None \
            ,
    ) \
:
    MePopenProcess00env0 \
        = \
        dict \
        (
        )
    MePopenProcess00env0 \
    .update \
    (
        os \
        .environ \
    )
    MePopenProcess00env0 \
    .update \
    (
        {
            'IPFS_PATH' \
            : \
                os \
                .path \
                .join \
                (
                    MeTwoPaths1 \
                        ,
                )
                    ,
        }
    )
    MeCheckOutputProcess00args0 \
        = \
        ' ' \
        .join \
        (
            [
                os \
                .path \
                .join \
                (
                    MeTwoPaths0 \
                        ,
                ) \
                    ,
                'repo' \
                    ,
                'gc' \
                    ,
                '--silent' \
                    ,
                '--' \
                    ,
            ] \
                ,
        )
    MeCheckOutputProcess00 \
        = \
        subprocess \
        .check_output \
        (
            MeCheckOutputProcess00args0 \
                ,
            cwd \
                = \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                )
                ,
            env \
                = \
                MePopenProcess00env0 \
                ,
            universal_newlines \
                = \
                False \
                ,
            shell \
                = \
                True \
                ,
        )
#_____________________________________________________________________
#_____________________________________________________________________
try \
:
    MeHaveTxtFile \
    (
    )
    MeKuboFilesLs \
    (
    )
except \
:
    if \
        str \
        (
            sys \
            .exception \
            (
            ) \
        ) \
        .find \
        (
            '233' \
        ) \
            != \
            -1 \
    :
        sys \
        .exit \
        (
        )
#_____________________________________________________________________
#_____________________________________________________________________
def \
    main \
    (
    ) \
:
    pass

if \
    __name__ \
        == \
        '__main__' \
:
    main \
    (
    )
#_____________________________________________________________________
