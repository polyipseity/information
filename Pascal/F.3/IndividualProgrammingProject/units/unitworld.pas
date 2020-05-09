unit UnitWorld;

{$mode objfpc}{$H+}
{$modeSwitch AdvancedRecords}

interface

uses
  Classes, SysUtils,
  LCLType, OpenGLContext, Controls,
  fgl, Matrix, GL, GLU,
  UnitUtilities;

resourcestring
  ResStringEUnexpected = 'Unexpected';
  ResStringEIllegal = 'Illegal';

type
  { World: Forward }

  TEnumFacing = (FacingUp, FacingDown, FacingNorth, FacingEast, FacingSouth, FacingWest);
  TSetEnumFacing = set of TEnumFacing;
  TWorldDataRange = {$IFDEF Debug}0..16{$ELSE}0..64{$ENDIF};

  { TGPosition }

  generic TGPosition<T> = class
    private
      fx: T;
      fy: T;
      fz: T;
    public
      constructor Create(const x, y, z: T);
      property x: T read fx;
      property y: T read fy;
      property z: T read fz;
      function Clone: TGPosition; virtual;
      function Offset(Facing: TEnumFacing): TGPosition; virtual;
      function Up: TGPosition; virtual;
      function Down: TGPosition; virtual;
      function North: TGPosition; virtual;
      function East: TGPosition; virtual;
      function South: TGPosition; virtual;
      function West: TGPosition; virtual;
  end;
  TPositionInteger = specialize TGPosition<Integer>;

type
  TPositionGLdouble = specialize TGPosition<GLdouble>;
  TBlock = class;
  TWorld = class;
  TBlockAir = class;
  TBlockExist = class;
  TBlockOpaque = class;
  TBlockTranslucent = class;
  TArrayPositionInteger = array of TPositionInteger;

  { Renderer: Forward }

  TCamera = class;
  TBlockRenderer = class;
  TBlockRendererDefault = class;
  TBlockAirRenderer = class;
  TBlockOpaqueRenderer = class;
  TBlockTranslucentRenderer = class;
  TWorldRenderer = class;

  { TFPGMapVisibleKey }

  TFPGMapVisibleKey = record
    Value: TPositionInteger;
    class operator = (const Left, Right: TFPGMapVisibleKey): boolean; overload;
    class operator < (const Left, Right: TFPGMapVisibleKey): boolean; overload;
    class operator > (const Left, Right: TFPGMapVisibleKey): boolean; overload;
  end;
function CompareTFPGMapVisibleKey(const Left, Right: TFPGMapVisibleKey): Integer;

type
  TFPGMapVisible = specialize TFPGMap<TFPGMapVisibleKey, TSetEnumFacing>;

  { World }

  { TBlock }

  TBlock = class
    private
      FRenderer: TBlockRenderer;
    public
      constructor Create(const Renderer: TBlockRenderer = nil);
      procedure SetRenderer(const Renderer: TBlockRenderer);
      property Renderer: TBlockRenderer read FRenderer write SetRenderer;
      function IsAir: boolean; virtual; abstract;
      function IsOpaque: boolean; virtual; abstract;
      destructor Destroy; override;
  end;

  { TBlockAir }

  TBlockAir = class(TBlock)
    function IsAir: boolean; override;
    function IsOpaque: boolean; override;
  end;

  { TBlockExist }

  TBlockExist = class(TBlock)
    function IsAir: boolean; override;
  end;

  { TBlockOpaque }

  TBlockOpaque = class(TBlockExist)
    function IsOpaque: boolean; override;
  end;

  { TBlockTranslucent }

  TBlockTranslucent = class(TBlockExist)
    function IsOpaque: boolean; override;
  end;

  { TWorld }

  TFunctionWorldForeachBlock = function(Block: TBlock; Position: TPositionInteger; Arg: Pointer): TBlock;
  TFunctionWorldForeachBlockOfObject = function(Block: TBlock; Position: TPositionInteger; Arg: Pointer): TBlock of object;
  TFunctionBlockForeachNeighbor = function(BlockTo, BlockFrom: TBlock; PositionTo, PositionFrom: TPositionInteger; Facing: TEnumFacing; Arg: Pointer): TBlock;
  TFunctionBlockForeachNeighborOfObject = function(BlockTo, BlockFrom: TBlock; PositionTo, PositionFrom: TPositionInteger; Facing: TEnumFacing; Arg: Pointer): TBlock of object;
  TWorld = class
    private
      FRenderer: TWorldRenderer;
    public
      constructor Create(const Renderer: TWorldRenderer = nil);
      procedure SetRenderer(const Renderer: TWorldRenderer);
      property Renderer: TWorldRenderer read FRenderer write SetRenderer;
      function GetBlock(const Position: TPositionInteger): TBlock; virtual;
      procedure SetBlock(const Position: TPositionInteger; const Block: TBlock); virtual;
      procedure ForeachBlock(const f: TFunctionWorldForeachBlock; const Arg: Pointer = nil); virtual; overload;
      procedure ForeachBlock(const f: TFunctionWorldForeachBlockOfObject; const Arg: Pointer = nil); virtual; overload;
      procedure ForeachNeighbor(const Position: TPositionInteger; const f: TFunctionBlockForeachNeighbor; const Arg: Pointer = nil); overload;
      procedure ForeachNeighbor(const Position: TPositionInteger; const f: TFunctionBlockForeachNeighborOfObject; const Arg: Pointer = nil); overload;
    private
      Data: array[TWorldDataRange, TWorldDataRange, TWorldDataRange] of TBlock;
      function InitializeData(Block: TBlock; Position: TPositionInteger; Arg: Pointer): TBlock;
    public
      destructor Destroy; override;
  end;

  { Renderer }

  { TCamera }

  TCamera = class
    public
      fov, zNear, zFar: GLdouble;
      constructor Create;
      procedure HandleRotateMouse(const Sender: TOpenGLControl; const Shift: TShiftState; const x, y: Integer);
      procedure HandleRotateKeyboard(const Sender: TOpenGLControl; const TimeDeltaMills: double);
      procedure UpdateRotation;
      procedure Move(const Sender: TOpenGLControl; const TimeDeltaMills: double);
      procedure Render(const Sender: TOpenGLControl);
      function GetPosition: Tvector3_double;
      destructor Destroy; override;
    private
      AxisX, AxisY, AxisZ: ^Tvector3_double;
      FPosition: ^Tvector3_double;
      Rotation: ^TQuaternionDouble;
      Front, Left, Up: ^Tvector3_double;
    public
      property Position: Tvector3_double read GetPosition;
  end;

  { TBlockRenderer }

  TBlockRenderer = class
    private
      FBlock: TBlock;
    public
      constructor Create(const Block: TBlock = nil);
      procedure SetBlock(const Block: TBlock);
      property Block: TBlock read FBlock write SetBlock;
      procedure Render(const Position: TPositionInteger; const Facings: TSetEnumFacing); virtual; abstract;
      destructor Destroy; override;
  end;

  { TBlockRendererDefault }

  TBlockRendererDefault = class(TBlockRenderer)
    public
      procedure Render(const Position: TPositionInteger; const Facings: TSetEnumFacing); override;
      procedure RenderUp(const Position: TPositionInteger); virtual;
      procedure RenderDown(const Position: TPositionInteger); virtual;
      procedure RenderNorth(const Position: TPositionInteger); virtual;
      procedure RenderEast(const Position: TPositionInteger); virtual;
      procedure RenderSouth(const Position: TPositionInteger); virtual;
      procedure RenderWest(const Position: TPositionInteger); virtual;
  end;

  { TBlockAirRenderer }

  TBlockAirRenderer = class(TBlockRendererDefault)
    public
      procedure Render(const Position: TPositionInteger; const Facings: TSetEnumFacing); override;
  end;

  { TBlockOpaqueRenderer }

  TBlockOpaqueRenderer = class(TBlockRendererDefault)
    public
      procedure Render(const Position: TPositionInteger; const Facings: TSetEnumFacing); override;
  end;

  { TBlockTranslucentRenderer }

  TBlockTranslucentRenderer = class(TBlockRendererDefault)
    public
      procedure Render(const Position: TPositionInteger; const Facings: TSetEnumFacing); override;
  end;

  { TWorldRenderer }

  TWorldRenderer = class
    private
      FWorld: TWorld;
      VisibleOpaque: TFPGMapVisible;
      VisibleTranslucent: TFPGMapVisible;
      function InitializeVisible(Block: TBlock; Position: TPositionInteger; Arg: Pointer): TBlock;
      function CheckNeighborBlockForVisible(BlockTo, BlockFrom: TBlock; PositionTo, PositionFrom: TPositionInteger; Facing: TEnumFacing; Arg: Pointer): TBlock;
    public
      constructor Create(const World: TWorld = nil);
      procedure SetWorld(const World: TWorld);
      property World: TWorld read FWorld write SetWorld;
      procedure Render;
      destructor Destroy; override;
  end;

  { Control }

  TKeyRange = 0..$FF;
  TSetKey = set of TKeyRange;

{ UnitWorld }

procedure OnResize0(const Sender: TOpenGLControl);
procedure Draw0(const Sender: TOpenGLControl);
procedure KeyDown0(const Sender: TOpenGLControl; var Key: Word; const Shift: TShiftState);
procedure KeyUp0(const Sender: TOpenGLControl; var Key: Word; const Shift: TShiftState);
procedure OnIdle0(const Sender: TOpenGLControl; var Done: boolean);
procedure OnClick0(const Sender: TOpenGLControl);
procedure OnMouseMove0(const Sender: TOpenGLControl; const Shift: TShiftState; const X, Y: Integer);
procedure OnMouseLeave0(const Sender: TOpenGLControl);

procedure MouseCapture(const Sender: TOpenGLControl);
procedure MouseUncapture(const Sender: TOpenGLControl);

const
  { World }
  SetWorldDataRange = [Low(TWorldDataRange)..High(TWorldDataRange)];
  { Render }
  { Control }
  SetKeyRange = [Low(TKeyRange)..High(TKeyRange)];
  KeysActive = [VK_W, VK_S, VK_A, VK_D, VK_Q, VK_E, VK_SPACE, VK_SHIFT];
  CameraMovementPerMills = 10 / MSecsPerSec;
  CameraRotationPerPixel = 90 / 800;
  CameraRotationPerMills = 90 / MSecsPerSec;

implementation

var
  RenderControlCenter: TPoint;
  TimeRenderedDay: TDateTime;
  KeysBeingPressed: TSetKey;
  MouseCaptured: boolean = false;

  Model, Proj: T16dArray;
  View: TViewPortArray;
  ICamera: TCamera;
  IWorld: TWorld;
  IWorldRenderer: TWorldRenderer;
  IBlockAir: TBlock;
  IBlockAirRenderer: TBlockRenderer;
  IBlockOpaque: TBlock;
  IBlockOpaqueRenderer: TBlockRenderer;
  IBlockTranslucent: TBlock;
  IBlockTranslucentRenderer: TBlockRenderer;

{ UnitWorld }

operator mod(const a, b: double) c: double; inline;
begin
  c:=a - b * int(a / b);
end;

{ World }

{ TGPosition }

constructor TGPosition.Create(const x, y, z: T);
begin
  fx:=x;
  fy:=y;
  fz:=z;
end;
function TGPosition.Clone: TGPosition;
begin
  exit(TGPosition.Create(x, y, z));
end;
function TGPosition.Offset(Facing: TEnumFacing): TGPosition;
begin
  case Facing of
    FacingUp: exit(Up);
    FacingDown: exit(Down);
    FacingNorth: exit(North);
    FacingEast: exit(East);
    FacingSouth: exit(South);
    FacingWest: exit(West);
    else raise EAbort(ResStringEUnexpected);
  end;
end;
function TGPosition.Up: TGPosition;
begin
  exit(TGPosition.Create(x, y, z + 1));
end;
function TGPosition.Down: TGPosition;
begin
  exit(TGPosition.Create(x, y, z - 1));
end;
function TGPosition.North: TGPosition;
begin
  exit(TGPosition.Create(x + 1, y, z));
end;
function TGPosition.East: TGPosition;
begin
  exit(TGPosition.Create(x, y - 1, z));
end;
function TGPosition.South: TGPosition;
begin
  exit(TGPosition.Create(x - 1, y, z));
end;
function TGPosition.West: TGPosition;
begin
  exit(TGPosition.Create(x, y + 1, z));
end;

{ TFPGMapVisibleKey }

class operator TFPGMapVisibleKey.= (const Left, Right: TFPGMapVisibleKey): boolean;
begin
  Result:=(Left.Value.x = Right.Value.x) and (Left.Value.y = Right.Value.y) and (Left.Value.z = Right.Value.z);
end;
class operator TFPGMapVisibleKey.< (const Left, Right: TFPGMapVisibleKey): boolean;
var
  LeftPosition: Tvector3_double;
  RightPosition: Tvector3_double;
begin
  with Left.Value do LeftPosition.Init(x, y, z);
  with Right.Value do RightPosition.Init(x, y, z);
  Result:=(LeftPosition - ICamera.Position).Squared_Length > (RightPosition - ICamera.Position).Squared_Length;
end;
class operator TFPGMapVisibleKey.> (const Left, Right: TFPGMapVisibleKey): boolean;
var
  LeftPosition: Tvector3_double;
  RightPosition: Tvector3_double;
begin
  with Left.Value do LeftPosition.Init(x, y, z);
  with Right.Value do RightPosition.Init(x, y, z);
  Result:=(LeftPosition - ICamera.Position).Squared_Length < (RightPosition - ICamera.Position).Squared_Length;
end;
function CompareTFPGMapVisibleKey(const Left, Right: TFPGMapVisibleKey): Integer;
begin
   if Left = Right then exit(0)
  else if Left < Right then exit(-1)
  else { if Left > Right then } exit(1);
end;

{ TBlock }

constructor TBlock.Create(const Renderer: TBlockRenderer = nil);
begin
  Self.Renderer:=Renderer;
end;
procedure TBlock.SetRenderer(const Renderer: TBlockRenderer);
begin
  if (Self.Renderer <> nil) and (Renderer <> nil) then raise EAbort.Create(ResStringEIllegal);
  FRenderer:=Renderer;
end;
destructor TBlock.Destroy;
begin
  try
    if Renderer <> nil then
    begin
      Renderer.Block:=nil;
      Renderer.Destroy;
    end;
  finally
    inherited;
  end;
end;

{ TBlockAir }

function TBlockAir.IsAir: boolean;
begin
  exit(true);
end;
function TBlockAir.IsOpaque: boolean;
begin
  exit(false);
end;

{ TBlockExist }

function TBlockExist.IsAir: boolean;
begin
  exit(false);
end;

function TBlockOpaque.IsOpaque: boolean;
begin
  exit(true);
end;

{ TBlockTranslucent }

function TBlockTranslucent.IsOpaque: boolean;
begin
  exit(false);
end;

{ TWorld }

constructor TWorld.Create(const Renderer: TWorldRenderer = nil);
begin
  ForeachBlock(@InitializeData);
  Self.Renderer:=Renderer;
end;
procedure TWorld.SetRenderer(const Renderer: TWorldRenderer);
begin
  if (Self.Renderer <> nil) and (Renderer <> nil) then raise EAbort.Create(ResStringEIllegal);
  FRenderer:=Renderer;
end;
function TWorld.InitializeData(Block: TBlock; Position: TPositionInteger; Arg: Pointer): TBlock;
begin
  case Random(3) of
    0: exit(IBlockAir);
    1: exit(IBlockOpaque);
    2: exit(IBlockTranslucent);
    else raise EAbort.Create(ResStringEUnexpected);
  end;
end;
function TWorld.GetBlock(const Position: TPositionInteger): TBlock;
begin
  if (Position.x in SetWorldDataRange) and (Position.y in SetWorldDataRange) and (Position.z in SetWorldDataRange) then
  begin
    exit(Data[Position.x][Position.z][Position.y]);
  end
  else exit(nil);
end;
procedure TWorld.SetBlock(const Position: TPositionInteger; const Block: TBlock);
begin
  if Block = nil then exit;
  if (Position.x in SetWorldDataRange) and (Position.y in SetWorldDataRange) and (Position.z in SetWorldDataRange) then
  begin
    Data[Position.x][Position.z][Position.y]:=Block;
  end;
end;
procedure TWorld.ForeachBlock(const f: TFunctionWorldForeachBlock; const Arg: Pointer = nil);
var
  x, y, z: TWorldDataRange;
  Position: TPositionInteger;
begin
  for x in SetWorldDataRange do
  begin
    for z in SetWorldDataRange do
    begin
      for y in SetWorldDataRange do
      begin
        Position:=TPositionInteger.Create(x, y, z);
        try
          SetBlock(Position, f(GetBlock(Position), Position, Arg));
        finally
          Position.Destroy;
        end;
      end;
    end;
  end;
end;
procedure TWorld.ForeachBlock(const f: TFunctionWorldForeachBlockOfObject; const Arg: Pointer = nil);
var
  x, y, z: TWorldDataRange;
  Position: TPositionInteger;
begin
  for x in SetWorldDataRange do
  begin
    for z in SetWorldDataRange do
    begin
      for y in SetWorldDataRange do
      begin
        Position:=TPositionInteger.Create(x, y, z);
        try
          SetBlock(Position, f(GetBlock(Position), Position, Arg));
        finally
          Position.Destroy;
        end;
      end;
    end;
  end;
end;
procedure TWorld.ForeachNeighbor(const Position: TPositionInteger; const f: TFunctionBlockForeachNeighbor; const Arg: Pointer = nil);
var
  BlockFrom: TBlock;
  Facing: TEnumFacing;
  PositionTo: TPositionInteger;
begin
  BlockFrom:=GetBlock(Position);
  for Facing in TEnumFacing do
  begin
    PositionTo:=Position.Offset(Facing);
    try
      SetBlock(PositionTo, f(GetBlock(PositionTo), BlockFrom, PositionTo, Position, Facing, Arg));
    finally
      PositionTo.Destroy;
    end;
  end;
end;
procedure TWorld.ForeachNeighbor(const Position: TPositionInteger; const f: TFunctionBlockForeachNeighborOfObject; const Arg: Pointer = nil);
var
  BlockFrom: TBlock;
  Facing: TEnumFacing;
  PositionTo: TPositionInteger;
begin
  BlockFrom:=GetBlock(Position);
  for Facing in TEnumFacing do
  begin
    PositionTo:=Position.Offset(Facing);
    try
      SetBlock(PositionTo, f(GetBlock(PositionTo), BlockFrom, PositionTo, Position, Facing, Arg));
    finally
      PositionTo.Destroy;
    end;
  end;
end;
destructor TWorld.Destroy;
begin
  try
    if Renderer <> nil then
    begin
      Renderer.World:=nil;
      Renderer.Destroy;
    end;
  finally
    inherited;
  end;
end;

{ Renderer }

{ TCamera }

constructor TCamera.Create;
var
  WorldCenter: double;
begin
  WorldCenter:=(Low(TWorldDataRange) + High(TWorldDataRange)) / 2;

  New(AxisX, Init(1, 0, 0));
  New(AxisY, Init(0, 1, 0));
  New(AxisZ, Init(0, 0, 1));

  fov:=90;
  zNear:=0.1;
  zFar:=1000;

  New(FPosition, Init(WorldCenter, WorldCenter, High(TWorldDataRange) + 2));
  New(Rotation, InitAngleAxis(0, AxisX^));
  New(Front);
  Front^:=AxisX^;
  New(Left);
  Left^:=AxisY^;
  New(Up);
  Up^:=AxisZ^;
end;
function TCamera.GetPosition: Tvector3_double;
begin
  exit(FPosition^);
end;
procedure TCamera.HandleRotateMouse(const Sender: TOpenGLControl; const Shift: TShiftState; const x, y: Integer);
var
  QYaw, QPitch: TQuaternionDouble;
begin
  QYaw.InitAngleAxis(CameraRotationPerPixel * (x - RenderControlCenter.x), -Up^);
  QPitch.InitAngleAxis(CameraRotationPerPixel * (y - RenderControlCenter.y), Left^);
  Rotation^:=(QYaw * (QPitch * Rotation^).Normalize).Normalize;
  Mouse.CursorPos:=Sender.ControlToScreen(RenderControlCenter);
  Sender.Invalidate;
end;
procedure TCamera.HandleRotateKeyboard(const Sender: TOpenGLControl; const TimeDeltaMills: double);
var
  CameraRotation: double;
  RollDiff: double = 0;
  QRoll: TQuaternionDouble;
begin
  CameraRotation:=CameraRotationPerMills * TimeDeltaMills;
  if VK_Q in KeysBeingPressed then RollDiff:=RollDiff - CameraRotation;
  if VK_E in KeysBeingPressed then RollDiff:=RollDiff + CameraRotation;
  QRoll.InitAngleAxis(RollDiff, Front^);
  Rotation^:=(QRoll * Rotation^).Normalize;
end;
procedure TCamera.UpdateRotation;
begin
  with TMatrixUtilities do
  begin
    Front^:=Normalize(Rotation^ * AxisX^);
    Left^:=Normalize(Rotation^ * AxisY^);
    Up^:=Normalize(Rotation^ * AxisZ^);
  end;
end;
procedure TCamera.Move(const Sender: TOpenGLControl; const TimeDeltaMills: double);
var
  CameraMovement: double;
begin
  CameraMovement:=CameraMovementPerMills * TimeDeltaMills;
  with TMatrixUtilities do
  begin
    if VK_W in KeysBeingPressed then FPosition^:=Position + Front^ * CameraMovement;
    if VK_S in KeysBeingPressed then FPosition^:=Position - Front^ * CameraMovement;
    if VK_A in KeysBeingPressed then FPosition^:=Position + Left^ * CameraMovement;
    if VK_D in KeysBeingPressed then FPosition^:=Position - Left^ * CameraMovement;
    if VK_SPACE in KeysBeingPressed then FPosition^:=Position + Up^ * CameraMovement;
    if VK_SHIFT in KeysBeingPressed then FPosition^:=Position - Up^ * CameraMovement;
  end;
  IWorld.Renderer.VisibleTranslucent.Sorted:=false;
end;
procedure TCamera.Render(const Sender: TOpenGLControl);
begin
  glMatrixMode(GL_PROJECTION);
  glLoadIdentity;
  with Sender do gluPerspective(fov, Width / Height, zNear, zFar);

  glMatrixMode(GL_MODELVIEW);
  glLoadIdentity;
  with Position do
    gluLookAt(Data[v3x], Data[v3y], Data[v3z],
              Data[v3x] + Front^.Data[v3x], Data[v3y] + Front^.Data[v3y], Data[v3z] + Front^.Data[v3z],
              Up^.Data[v3x], Up^.Data[v3y], Up^.Data[v3z]);

  glGetDoublev(GL_MODELVIEW_MATRIX, @Model);
  glGetDoublev(GL_PROJECTION_MATRIX, @Proj);
  glGetIntegerv(GL_VIEWPORT, @View);
end;
destructor TCamera.Destroy;
begin
  try
    Dispose(AxisX);
    Dispose(AxisY);
    Dispose(AxisZ);

    Dispose(FPosition);
    Dispose(Rotation, CleanUp);
    Dispose(Front);
    Dispose(Left);
    Dispose(Up);
  finally
    inherited;
  end;
end;

{ TBlockRenderer }

constructor TBlockRenderer.Create(const Block: TBlock);
begin
  Self.Block:=Block;
end;
procedure TBlockRenderer.SetBlock(const Block: TBlock);
begin
  if (Self.Block <> nil) and (Block <> nil) then raise EAbort.Create(ResStringEIllegal);
  FBlock:=Block;
end;
destructor TBlockRenderer.Destroy;
begin
  try
    if Block <> nil then
    begin
      Block.Renderer:=nil;
      Block.Destroy;
    end;
  finally
    inherited;
  end;
end;

{ TBlockRendererDefault }

procedure TBlockRendererDefault.Render(const Position: TPositionInteger; const Facings: TSetEnumFacing);
begin
  if FacingUp in Facings then RenderUp(Position);
  if FacingDown in Facings then RenderDown(Position);
  if FacingNorth in Facings then RenderNorth(Position);
  if FacingEast in Facings then RenderEast(Position);
  if FacingSouth in Facings then RenderSouth(Position);
  if FacingWest in Facings then RenderWest(Position);
end;
procedure TBlockRendererDefault.RenderUp(const Position: TPositionInteger);
begin
  with Position do
  begin
    glVertex3i(    x,     y, z + 1);
    glVertex3i(x + 1,     y, z + 1);
    glVertex3i(x + 1, y + 1, z + 1);
    glVertex3i(    x, y + 1, z + 1);
  end;
end;
procedure TBlockRendererDefault.RenderDown(const Position: TPositionInteger);
begin
  with Position do
  begin
    glVertex3i(    x,     y, z);
    glVertex3i(    x, y + 1, z);
    glVertex3i(x + 1, y + 1, z);
    glVertex3i(x + 1,     y, z);
  end;
end;
procedure TBlockRendererDefault.RenderNorth(const Position: TPositionInteger);
begin
  with Position do
  begin
    glVertex3i(x + 1,     y,     z);
    glVertex3i(x + 1, y + 1,     z);
    glVertex3i(x + 1, y + 1, z + 1);
    glVertex3i(x + 1,     y, z + 1);
  end;
end;
procedure TBlockRendererDefault.RenderEast(const Position: TPositionInteger);
begin
  with Position do
  begin
    glVertex3i(    x, y,     z);
    glVertex3i(x + 1, y,     z);
    glVertex3i(x + 1, y, z + 1);
    glVertex3i(    x, y, z + 1);
  end;
end;
procedure TBlockRendererDefault.RenderSouth(const Position: TPositionInteger);
begin
  with Position do
  begin
    glVertex3i(x,     y,     z);
    glVertex3i(x,     y, z + 1);
    glVertex3i(x, y + 1, z + 1);
    glVertex3i(x, y + 1,     z);
  end;
end;
procedure TBlockRendererDefault.RenderWest(const Position: TPositionInteger);
begin
  with Position do
  begin
    glVertex3i(    x, y + 1,     z);
    glVertex3i(    x, y + 1, z + 1);
    glVertex3i(x + 1, y + 1, z + 1);
    glVertex3i(x + 1, y + 1,     z);
  end;
end;

{ TBlockAirRenderer }

procedure TBlockAirRenderer.Render(const Position: TPositionInteger; const Facings: TSetEnumFacing);
begin
  // NOOP
end;

{ TBlockOpaqueRenderer }

procedure TBlockOpaqueRenderer.Render(const Position: TPositionInteger; const Facings: TSetEnumFacing);
begin
  glColor3d(Random, Random, Random);
  inherited;
end;

{ TBlockTranslucentRenderer }

procedure TBlockTranslucentRenderer.Render(const Position: TPositionInteger; const Facings: TSetEnumFacing);
begin
  glColor4d(Random, Random, Random, 0.5);
  inherited;
end;

{ TWorldRenderer }

constructor TWorldRenderer.Create(const World: TWorld = nil);
begin
  VisibleOpaque:=TFPGMapVisible.Create;
  VisibleOpaque.OnKeyCompare:=@CompareTFPGMapVisibleKey;
  VisibleTranslucent:=TFPGMapVisible.Create;
  VisibleTranslucent.OnKeyCompare:=@CompareTFPGMapVisibleKey;
  Self.World:=World;
end;
procedure TWorldRenderer.SetWorld(const World: TWorld);
begin
  if (Self.World <> nil) and (World <> nil) then raise EAbort.Create(ResStringEIllegal);
  FWorld:=World;
  if Self.World <> nil then Self.World.ForeachBlock(@InitializeVisible);
end;
function TWorldRenderer.InitializeVisible(Block: TBlock; Position: TPositionInteger; Arg: Pointer): TBlock;
begin
  World.ForeachNeighbor(Position, @CheckNeighborBlockForVisible);
  exit(Block);
end;
function TWorldRenderer.CheckNeighborBlockForVisible(BlockTo, BlockFrom: TBlock; PositionTo, PositionFrom: TPositionInteger; Facing: TEnumFacing; Arg: Pointer): TBlock;
var
  Visible: TFPGMapVisible;
  Key: TFPGMapVisibleKey;
  Index: Integer;
  Facings: TSetEnumFacing;
begin
  if (BlockTo = nil) or (not BlockTo.IsOpaque) then
  begin
    if BlockFrom.IsOpaque then Visible:=VisibleOpaque
    else Visible:=VisibleTranslucent;
    Key.Value:=PositionFrom;
    Index:=Visible.IndexOf(Key);
    if Index = -1 then
    begin
      Key.Value:=Key.Value.Clone;
      Index:=Visible.Add(Key);
      Visible.Sorted:=false;
    end
    else Facings:=Visible.Data[Index];
    Include(Facings, Facing);
    Visible.Data[Index]:=Facings;
  end;
  exit(BlockTo);
end;
procedure TWorldRenderer.Render;
var
  i: Integer;
begin
  glEnable(GL_CULL_FACE);
  glEnable(GL_DEPTH_TEST);
  glEnable(GL_BLEND);
  glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);

  glBegin(GL_QUADS);
  with VisibleOpaque do
  begin
    for i:=0 to Count - 1 do World.GetBlock(Keys[i].Value).Renderer.Render(Keys[i].Value, Data[i]);
  end;
  VisibleTranslucent.Sorted:=true;
  with VisibleTranslucent do
  begin
    for i:=0 to Count - 1 do World.GetBlock(Keys[i].Value).Renderer.Render(Keys[i].Value, Data[i]);
  end;
  glEnd;

  glDisable(GL_BLEND);
  glDisable(GL_DEPTH_TEST);
  glDisable(GL_CULL_FACE);
end;
destructor TWorldRenderer.Destroy;
var
  i: Integer;
begin
  try
    with VisibleOpaque do
    begin
      for i:=0 to Count - 1 do Keys[i].Value.Destroy;
    end;
    VisibleOpaque.Destroy;
    with VisibleTranslucent do
    begin
      for i:=0 to Count - 1 do Keys[i].Value.Destroy;
    end;
    VisibleTranslucent.Destroy;
    if World <> nil then
    begin
      World.Renderer:=nil;
      World.Destroy;
    end;
  finally
    inherited;
  end;
end;

{ UnitWorld }

{ Render }

procedure OnResize0(const Sender: TOpenGLControl);
begin
  with RenderControlCenter do
  begin
    with Sender do
    begin
      x:=Left + Width div 2;
      y:=Top + Height div 2;
    end;
  end;
end;
procedure Draw0(const Sender: TOpenGLControl);
var
  TimeDeltaMills: double;
begin
  TimeDeltaMills:=MSecsPerDay * (Now - TimeRenderedDay);
  TimeRenderedDay:=Now;
  glClearColor(0.52, 0.80, 0.92, 1.0); // Sky
  glClear(GL_COLOR_BUFFER_BIT or GL_DEPTH_BUFFER_BIT);
  with ICamera do
  begin
    HandleRotateKeyboard(Sender, TimeDeltaMills);
    UpdateRotation;
    Move(Sender, TimeDeltaMills);
    Render(Sender);
  end;
  IWorldRenderer.Render;
  Sender.SwapBuffers;
end;

{ Control }

procedure KeyDown0(const Sender: TOpenGLControl; var Key: word; const Shift: TShiftState);
begin
  case Key of
    VK_TAB: MouseUncapture(Sender);
  end;
  if not (Key in SetKeyRange) then exit;
  Sender.Refresh;
  Include(KeysBeingPressed, Key);
end;
procedure KeyUp0(const Sender: TOpenGLControl; var Key: word; const Shift: TShiftState);
begin
  if not (Key in SetKeyRange) then exit;
  Exclude(KeysBeingPressed, Key);
end;
procedure OnIdle0(const Sender: TOpenGLControl; var Done: boolean);
var
  Key: word;
begin
  Done:=true;
  for Key in KeysActive do
  begin
    if Key in KeysBeingPressed then
    begin
      Sender.Invalidate;
      break;
    end;
  end;
end;
procedure OnClick0(const Sender: TOpenGLControl);
begin
  MouseCapture(Sender);
end;
procedure OnMouseMove0(const Sender: TOpenGLControl; const Shift: TShiftState; const x, y: Integer);
begin
  if MouseCaptured then ICamera.HandleRotateMouse(Sender, Shift, x, y);
end;
procedure OnMouseLeave0(const Sender: TOpenGLControl);
begin
  if MouseCaptured then MouseUncapture(Sender);
end;

procedure MouseCapture(const Sender: TOpenGLControl);
begin
  SetCaptureControl(Sender);
  MouseCaptured:=true;
  Mouse.CursorPos:=Sender.ControlToScreen(RenderControlCenter);
  {$IFNDEF Debug}
  Sender.Cursor:=crNone;
  {$ENDIF}
end;
procedure MouseUncapture(const Sender: TOpenGLControl);
begin
  SetCaptureControl(nil);
  MouseCaptured:=false;
  Sender.Cursor:=crDefault;
end;

initialization
  ICamera:=TCamera.Create;

  IBlockAirRenderer:=TBlockAirRenderer.Create;
  IBlockAir:=TBlockAir.Create(IBlockAirRenderer);
  IBlockAirRenderer.Block:=IBlockAir;
  IBlockOpaqueRenderer:=TBlockOpaqueRenderer.Create;
  IBlockOpaque:=TBlockOpaque.Create(IBlockOpaqueRenderer);
  IBlockOpaqueRenderer.Block:=IBlockOpaque;
  IBlockTranslucentRenderer:=TBlockTranslucentRenderer.Create;
  IBlockTranslucent:=TBlockTranslucent.Create(IBlockTranslucentRenderer);
  IBlockTranslucentRenderer.Block:=IBlockTranslucent;

  IWorldRenderer:=TWorldRenderer.Create;
  IWorld:=TWorld.Create(IWorldRenderer);
  IWorldRenderer.World:=IWorld;

  TimeRenderedDay:=Now;

finalization
  ICamera.Destroy;
  IWorld.Destroy;
  IBlockAir.Destroy;
  IBlockOpaque.Destroy;
  IBlockTranslucent.Destroy;

end.

