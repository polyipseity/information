#version 330 core

layout (location=0) in vec4 vPos;
layout (location=1) in vec4 vClr;

out vec4 fClr;

uniform mat4 uProjectionMat, uModelViewMat;

void main() {
  gl_Position = uProjectionMat * uModelViewMat * vPos;
  fClr = vClr;
}

