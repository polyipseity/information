unit UnitUtilities;

{$mode objfpc}{$H+}
{$modeSwitch AdvancedRecords}

interface

uses
  Classes, SysUtils,
  Matrix, Math, fgl,
  dglOpenGL;

type
  { Utilities }
  TArrayDouble = specialize TArray<double>;

  { TQuaternionDouble }

  TQuaternionDouble = record
    public
      w, x, y, z: double;
      constructor Init(const ww, xx, yy, zz: double); overload;
      constructor Init_AxisAngle(const AxisX, AxisY, AxisZ, Angle: double); overload;
      constructor Init_AxisAngle(const Axis: Tvector3_double_data; const Angle: double); overload;
      constructor Init_AxisAngle(const Axis: Tvector3_double; const Angle: double); overload;
      function Norm: double;
      function Normalize: TQuaternionDouble;
      procedure Normalize(var Q: TQuaternionDouble);
      function Conjugate: TQuaternionDouble;
      procedure Conjugate(var Q: TQuaternionDouble);
      class operator + (const Left : TQuaternionDouble) Right: TQuaternionDouble; overload;
      class operator + (const Left, Right : TQuaternionDouble): TQuaternionDouble; overload;
      class operator + (const Left : TQuaternionDouble; const Right : double): TQuaternionDouble; overload;
      class operator + (const Left : double; const Right : TQuaternionDouble): TQuaternionDouble; overload;
      class operator - (const Left : TQuaternionDouble) Right: TQuaternionDouble; overload;
      class operator - (const Left, Right : TQuaternionDouble): TQuaternionDouble; overload;
      class operator * (const Left, Right : TQuaternionDouble): TQuaternionDouble; overload;
      class operator * (const Left: TQuaternionDouble; const Right: Tvector3_double): Tvector3_double; overload;
      class operator * (const Left : TQuaternionDouble; const Right : double): TQuaternionDouble; overload;
      class operator * (const Left : double; const Right : TQuaternionDouble): TQuaternionDouble; overload;
      class operator := (const Right: Tvector3_double) Left: TQuaternionDouble; overload;
      class operator := (const Right: TQuaternionDouble) Left: Tvector3_double; overload;
  end;
  PQuaternionDouble = ^TQuaternionDouble;

type
  { TMatrixUtilities }

  TMatrixUtilities = class
    class procedure Copy(out Output: Tvector3_double; const Input: Tvector3_double);
    class procedure Normalize(out Output: Tvector3_double; const Input: Tvector3_double);
  end;

  { TOpenGLUtilities }

  TOpenGLUtilities = class
    type
      TArrayGLuint = specialize TArray<GLuint>;
      TFPGListGLuint = specialize TFPGList<GLuint>;
      TFPGListArrayGLuint = array[0..MaxGListSize] of GLuint;
      PFPGListArrayGLuint = ^TFPGListArrayGLuint;
      TArrayGLfloat = specialize TArray<GLfloat>;
      TFPGListGLfloat = specialize TFPGList<GLfloat>;
      TFPGListArrayGLfloat = array[0..MaxGListSize] of GLfloat;
      PFPGListArrayGLfloat = ^TFPGListArrayGLfloat;
    class procedure ObjectLabel(const Identifier: GLenum; const Name: GLuint; const Label_: string);
    class procedure Translated2(var Input: Tmatrix4_double; const x, y, z: GLdouble);
    class procedure Frustumd2(var Projection: Tmatrix4_double; const Left, Right, Bottom, Top, ZNear, ZFar: GLdouble);
    class procedure Perspectived2(var Projection: Tmatrix4_double; const fovY, Aspect, ZNear, ZFar: GLdouble);
    class procedure LookAtd2(var ModelView: Tmatrix4_double; const Eye, Center, Up: Tvector3_double);
  end;

  { TProcedurePointer }
  TProcedurePointerProcedurePointer = procedure(Pointer: PtrInt);
  TProcedurePointer = class
    public
      constructor Create(const Proc: TProcedurePointerProcedurePointer);
      procedure Destroy(Pointer: PtrInt); overload;
      procedure Run(Pointer: PtrInt);
    public
      Proc: TProcedurePointerProcedurePointer;
  end;

  { TThreadUtilities }
  TThreadUtilities = class
    public
      procedure AwaitSynchornize;
  end;

{ UnitUtilities }

operator mod (const a, b: double) c: double; inline;
operator = (const Left, Right: Tvector3_double): boolean; overload; inline;

var
  PointerNil: Pointer = Pointer(0);
  ObjectUnused: TObject;
  ThreadUtilities: TThreadUtilities;

const
  { Vector/Matrix }
  v3x = 0;
  v3y = 1;
  v3z = 2;
  { OpenGL }
  GL_LIGHTING = $0B50 deprecated;
  GL_VERTEX_ARRAY = $8074 deprecated;

implementation

{ TQuaternionDouble }

constructor TQuaternionDouble.Init(const ww, xx, yy, zz: double);
begin
  w:=ww;
  x:=xx;
  y:=yy;
  z:=zz;
end;
constructor TQuaternionDouble.Init_AxisAngle(const AxisX, AxisY, AxisZ, Angle: double);
var
  AngleRadHalved: ValReal;
  AngleRadHalvedSin: ValReal;
begin
  AngleRadHalved:=DegToRad(Angle) / 2;
  AngleRadHalvedSin:=sin(AngleRadHalved);
  Init(cos(AngleRadHalved), AngleRadHalvedSin * AxisX, AngleRadHalvedSin * AxisY, AngleRadHalvedSin * AxisZ);
  Normalize;
end;
constructor TQuaternionDouble.Init_AxisAngle(const Axis: Tvector3_double_data; const Angle: double);
begin
  Init_AxisAngle(Axis[v3x], Axis[v3y], Axis[v3z], Angle);
end;
constructor TQuaternionDouble.Init_AxisAngle(const Axis: Tvector3_double; const Angle: double);
begin
  Init_AxisAngle(Axis.Data, Angle);
end;
function TQuaternionDouble.Norm: double;
begin
  exit(sqrt(sqr(w) + sqr(x) + sqr(y) + sqr(z)));
end;
function TQuaternionDouble.Normalize: TQuaternionDouble;
begin
  Normalize(Self);
  exit(Self);
end;
procedure TQuaternionDouble.Normalize(var Q: TQuaternionDouble);
var
  Length: double;
begin
  Length:=Norm;
  Q.w:=w / Length;
  Q.x:=x / Length;
  Q.y:=y / Length;
  Q.z:=z / Length;
end;
function TQuaternionDouble.Conjugate: TQuaternionDouble;
begin
  Conjugate(Self);
  exit(Self);
end;
procedure TQuaternionDouble.Conjugate(var Q: TQuaternionDouble);
begin
  Q:=Self;
  Q.x:=-x;
  Q.y:=-y;
  Q.z:=-z;
end;
class operator TQuaternionDouble.+ (const Left: TQuaternionDouble) Right: TQuaternionDouble;
begin
  Right:=Left;
end;
class operator TQuaternionDouble.+ (const Left, Right: TQuaternionDouble): TQuaternionDouble;
begin
  Result.w:=Left.w + Right.w;
  Result.x:=Left.x + Right.x;
  Result.y:=Left.y + Right.y;
  Result.z:=Left.z + Right.z;
end;
class operator TQuaternionDouble.+ (const Left: TQuaternionDouble; const Right: double): TQuaternionDouble;
begin
  Result:=Left;
  Result.w:=Result.w + Right;
end;
class operator TQuaternionDouble.+ (const Left: double; const Right: TQuaternionDouble): TQuaternionDouble;
begin
  Result:=Right;
  Result.w:=Left + Result.w;
end;
class operator TQuaternionDouble.- (const Left: TQuaternionDouble) Right: TQuaternionDouble;
begin
  Right.w:=-Left.w;
  Right.x:=-Left.x;
  Right.y:=-Left.y;
  Right.z:=-Left.z;
end;
class operator TQuaternionDouble.- (const Left, Right: TQuaternionDouble): TQuaternionDouble;
begin
  Result.w:=Left.w - Right.w;
  Result.x:=Left.x - Right.x;
  Result.y:=Left.y - Right.y;
  Result.z:=Left.z - Right.z;
end;
class operator TQuaternionDouble.* (const Left: TQuaternionDouble; const Right: Tvector3_double): Tvector3_double;
var
  QRight, CLeft: TQuaternionDouble;
begin
  QRight:=Right;
  Left.Conjugate(CLeft);
  Result:=((Left * QRight).Normalize * CLeft).Normalize;
end;
class operator TQuaternionDouble.* (const Left, Right: TQuaternionDouble): TQuaternionDouble;
begin
  Result.w:=Left.w * Right.w - Left.x * Right.x - Left.y * Right.y - Left.z * Right.z;
  Result.x:=Left.w * Right.x + Left.x * Right.w + Left.y * Right.z - Left.z * Right.y;
  Result.y:=Left.w * Right.y - Left.x * Right.z + Left.y * Right.w + Left.z * Right.x;
  Result.z:=Left.w * Right.z + Left.x * Right.y - Left.y * Right.x + Left.z * Right.w;
end;
class operator TQuaternionDouble.* (const Left: double; const Right: TQuaternionDouble): TQuaternionDouble;
begin
  Result.w:=Left * Right.w;
  Result.x:=Left * Right.x;
  Result.y:=Left * Right.y;
  Result.z:=Left * Right.z;
end;
class operator TQuaternionDouble.* (const Left: TQuaternionDouble; const Right: double): TQuaternionDouble;
begin
  Result.w:=Left.w * Right;
  Result.x:=Left.x * Right;
  Result.y:=Left.y * Right;
  Result.z:=Left.z * Right;
end;
class operator TQuaternionDouble.:= (const Right: Tvector3_double) Left: TQuaternionDouble;
begin
  with Right do
  begin
    Left.w:=0;
    Left.x:=Data[v3x];
    Left.y:=Data[v3y];
    Left.z:=Data[v3z];
  end;
end;
class operator TQuaternionDouble.:= (const Right: TQuaternionDouble) Left: Tvector3_double;
begin
  with Right do Left.Init(x, y, z);
end;

{ TMatrixUtilities }

class procedure TMatrixUtilities.Copy(out Output: Tvector3_double; const Input: Tvector3_double);
begin
  with Input do Output.Init(Data[v3x], Data[v3y], Data[v3z]);
end;

class procedure TMatrixUtilities.Normalize(out Output: Tvector3_double; const Input: Tvector3_double);
begin
  Copy(Output, Input / Input.Length);
end;

{ TOpenGLUtilities }

class procedure TOpenGLUtilities.ObjectLabel(const Identifier: GLenum; const Name: GLuint; const Label_: AnsiString);
var
  PLabel: PGLchar;
begin
  PLabel:=PGLchar(Label_);
  glObjectLabel(Identifier, Name, -1, PLabel);
end;
class procedure TOpenGLUtilities.Translated2(var Input: Tmatrix4_double; const x, y, z: GLdouble);
var
  i: 0..3;
begin
  for i:=0 to 3 do Input.Data[3][i]:=Input.Data[0][i] * x + Input.Data[1][i] * y +  Input.Data[2][i] * z + Input.Data[3][i];
end;
class procedure TOpenGLUtilities.Frustumd2(var Projection: Tmatrix4_double; const Left, Right, Bottom, Top, ZNear, ZFar: GLdouble);
// https://www.khronos.org/opengl/wiki/GluPerspective_code
var
  ZNearDouble, Width, Height, ZDiff: GLdouble;
  Output: Tmatrix4_double;
begin
  ZNearDouble:=2 * ZNear;
  Width:=Right - Left;
  Height:=Top - Bottom;
  ZDiff:=ZFar - ZNear;
  Output.Init(   ZNearDouble / Width,                       0,                             0,  0,
                                   0,    ZNearDouble / Height,                             0,  0,
              (Right + Left) / Width, (Top + Bottom) / Height, (      -ZFar - ZNear) / ZDiff, -1,
                                   0,                       0, (-ZNearDouble * ZFar) / ZDiff,  0);
  Projection:=Projection * Output;
end;
class procedure TOpenGLUtilities.Perspectived2(var Projection: Tmatrix4_double; const fovY, Aspect, ZNear, ZFar: GLdouble);
// https://www.khronos.org/opengl/wiki/GluPerspective_code
var
  YMax, XMax { , YMin, XMin } : GLdouble;
begin
  YMax:=ZNear * tan(DegToRad(fovY));
  //YMin:=-YMax;
  //XMin:=-YMax * Aspect;
  XMax:=YMax * Aspect;
  Frustumd2(Projection, -XMax, XMax, -YMax, YMax, ZNear, ZFar);
end;
class procedure TOpenGLUtilities.LookAtd2(var ModelView: Tmatrix4_double; const Eye, Center, Up: Tvector3_double);
// https://www.khronos.org/opengl/wiki/GluLookAt_code
var
  Front, Side, Top: Tvector3_double;
  Matrix: Tmatrix4_double;
begin
  // --------------------
  TMatrixUtilities.Normalize(Front, Center - Eye);
  // --------------------
  // Side = forward x up
  TMatrixUtilities.Normalize(Side, Front >< Up);
  // --------------------
  // Recompute up as: up = side x forward
  TMatrixUtilities.Normalize(Top, Side >< Front);
  // --------------------
  Matrix.Init(Side.Data[0], Top.Data[0], -Front.Data[0], 0,
              Side.Data[1], Top.Data[1], -Front.Data[1], 0,
              Side.Data[2], Top.Data[2], -Front.Data[2], 0,
                         0,           0,              0, 1);
  // --------------------
  ModelView:=ModelView * Matrix;
  Translated2(ModelView, -Eye.Data[0], -Eye.Data[1], -Eye.Data[2]);
  // --------------------
end;

{ TProcedurePointerProcedurePointer }

constructor TProcedurePointer.Create(const Proc: TProcedurePointerProcedurePointer);
begin
  Self.Proc:=Proc;
end;
procedure TProcedurePointer.Destroy(Pointer: PtrInt);
begin
  Destroy;
end;
procedure TProcedurePointer.Run(Pointer: PtrInt);
begin
  Proc(Pointer);
end;

{ TThreadUtilities }

procedure TThreadUtilities.AwaitSynchornize;
begin
  // NOOP
end;

{ UnitUtilities }

operator mod (const a, b: double) c: double;
begin
  c:=a - b * int(a / b);
end;

operator = (const Left, Right: Tvector3_double): boolean;
begin
  exit((Left.Data[v3x] = Right.Data[v3x]) and (Left.Data[v3y] = Right.Data[v3y]) and (Left.Data[v3z] = Right.Data[v3z]))
end;

initialization
  ObjectUnused:=TObject.Create;
  ThreadUtilities:=TThreadUtilities.Create;

finalization
  ObjectUnused.Destroy;
  ThreadUtilities.Destroy;

end.

