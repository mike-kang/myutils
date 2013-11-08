function findgyp()
{
  if [ $# -eq 0 ]; then
    python -c "import cfind; cfind.find_gyp()"
  else  
    python -c "import cfind; cfind.find_gyp('$1')"
  fi
}

function findc()
{
  if [ $# -eq 0 ]; then
    python -c "import cfind; cfind.find_c()"
  else 
    python -c "import cfind; cfind.find_c('$1')"
  fi
}

function findh()
{
  if [ $# -eq 0 ]; then
    python -c "import cfind; cfind.find_h()"
  else 
    python -c "import cfind; cfind.find_h('$1')"
  fi
}

function findj()
{
  if [ $# -eq 0 ]; then
    python -c "import cfind; cfind.find_java()"
  else  
    python -c "import cfind; cfind.find_java('$1')"
  fi
}

function cgrep()
{
  cat .c_list | xargs grep $1 2> /dev/null
}

function hgrep()
{
  cat .h_list | xargs grep $1 2> /dev/null
}

