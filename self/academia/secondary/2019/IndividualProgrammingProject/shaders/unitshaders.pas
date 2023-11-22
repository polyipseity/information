unit UnitShaders;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils,
  {$IFDEF Windows}Windows,{$ENDIF}
  Forms,
  dglOpenGL;

resourcestring
  ResStringOGLShaderCompileFailure = 'OpenGL Shader Compile Failure';
  ResStringOGLShaderProgramLinkFailure = 'OpenGL Shader Program Link Failure';

type
  TArrayShader = specialize TArray<GLhandle>;

function LoadShaderFromResourceName(const ResName: string): string;
function CompileShader(Shader: string; ShaderType: GLenum): GLHandle;
function LinkProgram(ShaderObjs: TArrayShader): GLhandle;

const
  OGLShaderVertex3D: string = 'OGLShaderVertex3D';
  OGLShaderVertex3DUniformProjectionMat = 'uProjectionMat';
  OGLShaderVertex3DUniformModelViewMat = 'uModelViewMat';
  OGLShaderFragementIdentity: string = 'OGLShaderFragementIdentity';

implementation

function LoadShaderFromResourceName(const ResName: string): string;
var
  ResS: TResourceStream;
begin
  ResS:=TResourceStream.Create(HInstance, ResName, RT_RCDATA);
  try
    SetString(Result, PChar(ResS.Memory), ResS.Size);
  finally
    ResS.Destroy;
  end;
end;

function CompileShader(Shader: string; ShaderType: GLenum): GLHandle;
var
  ShaderObj: GLHandle;
  Status, ErrorLength: GLInt;
  Error: string;
begin
  ShaderObj:=glCreateShader(ShaderType);
  glShaderSource(ShaderObj, 1, @Shader, nil);
  glCompileShader(ShaderObj);

  glGetShaderiv(ShaderObj, GL_COMPILE_STATUS, @Status);
  if Status = 0 then
  begin
    glGetShaderiv(ShaderObj, GL_INFO_LOG_LENGTH, @ErrorLength);
    SetLength(Error, ErrorLength + 1);
    glGetShaderInfoLog(ShaderObj, ErrorLength, nil, @Error[1]);
    Application.MessageBox(PChar(Error), PChar(ResStringOGLShaderCompileFailure), MB_ICONERROR);
    Halt;
  end;

  exit(ShaderObj);
end;

function LinkProgram(ShaderObjs: TArrayShader): GLhandle;
var
  ProgramObj, ShaderObj: GLhandle;
  Status, ErrorLength: GLInt;
  Error: string;
begin
  ProgramObj:=glCreateProgram();

  for ShaderObj in ShaderObjs do glAttachShader(ProgramObj, ShaderObj);
  glLinkProgram(ProgramObj);

  glGetProgramiv(ProgramObj, GL_LINK_STATUS, @Status);
  if Status = 0 then
  begin
    glGetProgramiv(ProgramObj, GL_INFO_LOG_LENGTH, @ErrorLength);
    SetLength(Error, ErrorLength + 1);
    glGetProgramInfoLog(ProgramObj, ErrorLength, nil, @Error[1]);
    Application.MessageBox(PChar(Error), PChar(ResStringOGLShaderProgramLinkFailure), MB_ICONERROR);
    Halt;
  end;

  exit(ProgramObj);
end;

end.

