unit UnitUtilities;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils,
  Matrix, Math;

type
  { TQuaternionDouble }

  TQuaternionDouble = object
    public
      w, x, y, z: double;
      constructor Init(const ww, xx, yy, zz: double); overload;
      constructor InitAngleAxis(const Angle, AxisX, AxisY, AxisZ: double); overload;
      constructor InitAngleAxis(const Angle: double; const Axis: Tvector3_double_data); overload;
      constructor InitAngleAxis(const Angle: double; const Axis: Tvector3_double); overload;
      destructor CleanUp;
      function Norm: double;
      function Normalize: TQuaternionDouble;
      function Conjugate: TQuaternionDouble;
  end;

  operator + (const Left : TQuaternionDouble) Right: TQuaternionDouble; overload;
  operator + (const Left, Right : TQuaternionDouble): TQuaternionDouble; overload;
  operator + (const Left : TQuaternionDouble; const Right : double): TQuaternionDouble; overload;
  operator + (const Left : double; const Right : TQuaternionDouble): TQuaternionDouble; overload;
  operator - (const Left : TQuaternionDouble) Right: TQuaternionDouble; overload;
  operator - (const Left, Right : TQuaternionDouble): TQuaternionDouble; overload;
  operator * (const Left, Right : TQuaternionDouble): TQuaternionDouble; overload;
  operator * (const Left: TQuaternionDouble; const Right: Tvector3_double): Tvector3_double; overload;
  operator * (const Left : TQuaternionDouble; const Right : double): TQuaternionDouble; overload;
  operator * (const Left : double; const Right : TQuaternionDouble): TQuaternionDouble; overload;
  operator := (const Right: Tvector3_double) Left: TQuaternionDouble; overload;
  operator := (const Right: TQuaternionDouble) Left: Tvector3_double; overload;

type
  { TMatrixUtilities }

  TMatrixUtilities = class
    class function Normalize(v: Tvector3_double): Tvector3_double; overload;
  end;

var
  ObjectUnused: TObject;

const
  v3x = 0;
  v3y = 1;
  v3z = 2;

implementation

{ TQuaternionDouble }

constructor TQuaternionDouble.Init(const ww, xx, yy, zz: double);
begin
  w:=ww;
  x:=xx;
  y:=yy;
  z:=zz;
end;
constructor TQuaternionDouble.InitAngleAxis(const Angle, AxisX, AxisY, AxisZ: double);
var
  AngleRadHalved: ValReal;
  AngleRadHalvedSin: ValReal;
begin
  AngleRadHalved:=DegToRad(Angle) / 2;
  AngleRadHalvedSin:=sin(AngleRadHalved);
  Init(cos(AngleRadHalved), AngleRadHalvedSin * AxisX, AngleRadHalvedSin * AxisY, AngleRadHalvedSin * AxisZ);
  Self:=Normalize;
end;
constructor TQuaternionDouble.InitAngleAxis(const Angle: double; const Axis: Tvector3_double_data);
begin
  InitAngleAxis(Angle, Axis[v3x], Axis[v3y], Axis[v3z]);
end;
constructor TQuaternionDouble.InitAngleAxis(const Angle: double; const Axis: Tvector3_double);
begin
  InitAngleAxis(Angle, Axis.Data);
end;
destructor TQuaternionDouble.CleanUp;
begin
  // NOOP
end;
function TQuaternionDouble.Norm: double;
begin
  exit(sqrt(sqr(w) + sqr(x) + sqr(y) + sqr(z)));
end;
function TQuaternionDouble.Normalize: TQuaternionDouble;
var
  Length: double;
  Normalized: TQuaternionDouble;
begin
  Length:=Norm;
  Normalized.Init(w / Length, x / Length, y / Length, z / Length);
  exit(Normalized);
end;
function TQuaternionDouble.Conjugate: TQuaternionDouble;
var
  Q: TQuaternionDouble;
begin
  Q:=Self;
  Q.x:=-x;
  Q.y:=-y;
  Q.z:=-z;
  exit(Q);
end;
operator + (const Left: TQuaternionDouble) Right: TQuaternionDouble;
begin
  Right:=Left;
end;
operator + (const Left, Right: TQuaternionDouble): TQuaternionDouble;
begin
  Result.w:=Left.w + Right.w;
  Result.x:=Left.x + Right.x;
  Result.y:=Left.y + Right.y;
  Result.z:=Left.z + Right.z;
end;
operator + (const Left: TQuaternionDouble; const Right: double): TQuaternionDouble;
begin
  Result:=Left;
  Result.w:=Result.w + Right;
end;
operator + (const Left: double; const Right: TQuaternionDouble): TQuaternionDouble;
begin
  Result:=Right;
  Result.w:=Left + Result.w;
end;
operator - (const Left: TQuaternionDouble) Right: TQuaternionDouble;
begin
  Right.w:=-Left.w;
  Right.x:=-Left.x;
  Right.y:=-Left.y;
  Right.z:=-Left.z;
end;
operator - (const Left, Right: TQuaternionDouble): TQuaternionDouble;
begin
  Result.w:=Left.w - Right.w;
  Result.x:=Left.x - Right.x;
  Result.y:=Left.y - Right.y;
  Result.z:=Left.z - Right.z;
end;
operator * (const Left: TQuaternionDouble; const Right: Tvector3_double): Tvector3_double;
var
  QRight: TQuaternionDouble;
begin
  QRight:=Right;
  exit(((Left * QRight).Normalize * Left.Conjugate).Normalize);
end;
operator * (const Left, Right: TQuaternionDouble): TQuaternionDouble;
begin
  Result.w:=Left.w * Right.w - Left.x * Right.x - Left.y * Right.y - Left.z * Right.z;
  Result.x:=Left.w * Right.x + Left.x * Right.w + Left.y * Right.z - Left.z * Right.y;
  Result.y:=Left.w * Right.y - Left.x * Right.z + Left.y * Right.w + Left.z * Right.x;
  Result.z:=Left.w * Right.z + Left.x * Right.y - Left.y * Right.x + Left.z * Right.w;
end;
operator * (const Left: double; const Right: TQuaternionDouble): TQuaternionDouble;
begin
  Result.w:=Left * Right.w;
  Result.x:=Left * Right.x;
  Result.y:=Left * Right.y;
  Result.z:=Left * Right.z;
end;
operator * (const Left: TQuaternionDouble; const Right: double): TQuaternionDouble;
begin
  Result.w:=Left.w * Right;
  Result.x:=Left.x * Right;
  Result.y:=Left.y * Right;
  Result.z:=Left.z * Right;
end;
operator := (const Right: Tvector3_double) Left: TQuaternionDouble;
begin
  with Right do
  begin
    Left.w:=0;
    Left.x:=Data[v3x];
    Left.y:=Data[v3y];
    Left.z:=Data[v3z];
  end;
end;
operator := (const Right: TQuaternionDouble) Left: Tvector3_double;
begin
  with Left do
  begin
    Data[v3x]:=Right.x;
    Data[v3y]:=Right.y;
    Data[v3z]:=Right.z;
  end;
end;

{ TMatrixUtilities }

class function TMatrixUtilities.Normalize(v: Tvector3_double): Tvector3_double;
begin
  exit(v / v.Length);
end;

initialization
  ObjectUnused:=TObject.Create;

finalization
  ObjectUnused.Destroy;

end.

