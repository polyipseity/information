unit UnitGame;

{$mode objfpc}{$H+}
{$modeSwitch AdvancedRecords}
{$modeSwitch NestedProcVars}
{$MACRO ON}

{$IFDEF Windows}
  {$DEFINE extdecl := stdcall}
{$ELSE}
  {$DEFINE extdecl := cdecl}
{$ENDIF}

interface

uses
  {$IFDEF UNIX}{$IFDEF UseCThreads}
  cthreads,
  {$ENDIF}{$ENDIF}
  Classes, SysUtils, Forms,
  LCLType, OpenGLContext, Controls, StdCtrls, ComCtrls,
  fgl, Matrix, dglOpenGL, MTProcs, Math,
  {$IFDEF Debug}GHashSet,{$ENDIF}
  UnitFormMain, UnitUtilities, UnitShaders;

resourcestring
  ResStringEUnexpected = 'Unexpected';
  ResStringEIllegal = 'Illegal';
  ResStringOGLObjLabelShaderVertex = 'Shader Vertex';
  ResStringOGLObjLabelShaderFragment = 'Shader Fragment';
  ResStringOGLObjLabelProgramShader = 'Program';
  ResStringOGLObjLabelChunkOpaqueVAO = 'Chunk Opaque VAO';
  ResStringOGLObjLabelChunkOpaqueEBO = 'Chunk Opaque EBO';
  ResStringOGLObjLabelChunkOpaqueVBOV = 'Chunk Opaque VBO Vertex';
  ResStringOGLObjLabelChunkOpaqueVBOC = 'Chunk Opaque VBO Color';
  ResStringOGLObjLabelChunkTranslucentVAO = 'Chunk Translucent VAO';
  ResStringOGLObjLabelChunkTranslucentEBO = 'Chunk Translucent EBO';
  ResStringOGLObjLabelChunkTranslucentVBOV = 'Chunk Translucent VBO Vertex';
  ResStringOGLObjLabelChunkTranslucentVBOC = 'Chunk Translucent VBO Color';
  ResStringOGLError = 'OpenGL Error';
  ResStringOGLErrorHeader = '*** OpenGL Error ***';
  ResStringOGLCallback = 'OpenGL Callback: ';
  ResStringOGLErrorSource = 'source';
  ResStringOGLErrorType = 'type';
  ResStringOGLErrorId = 'id';
  ResStringOGLErrorSeverity = 'severity';
  ResStringOGLErrorMessage = 'message';
  ResStringOGLErrorUserParam = 'user param';

type
  { Forward }

  { World: Forward }

  TEnumFacing = (FacingUp, FacingDown, FacingNorth, FacingEast, FacingSouth, FacingWest);
  TEnumPositionElement = (PositionX, PositionY, PositionZ);
  PEnumPositionElement = ^TEnumPositionElement;
  TSetEnumFacing = set of TEnumFacing;

  { TGPosition }

  generic TGPosition<T> = packed class
    protected
      fx: T;
      fy: T;
      fz: T;
    public
      constructor Create(const x, y, z: T);
      constructor Create_Zero;
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
  TGPositionInteger = specialize TGPosition<Integer>;
  TGPositionExtended = specialize TGPosition<extended>;
  PGPositionInteger = ^TGPositionInteger;
operator := (const Right: TGPositionInteger): TGPositionExtended; overload;
operator + (const Left, Right: TGPositionInteger): TGPositionInteger; overload;
operator + (const Left, Right: TGPositionExtended): TGPositionExtended; overload;
operator / (const Left: TGPositionExtended; const Right: extended): TGPositionExtended; overload;

type
  TPositionGLdouble = specialize TGPosition<GLdouble>;
  TBlock = class;
  TWorld = class;
  TBlockAir = class;
  TBlockExist = class;
  TBlockOpaque = class;
  TBlockTranslucent = class;

  { Renderer: Forward }

  TCamera = class;
  TBlockRenderer = class;
  TBlockRendererDefault = class;
  TBlockAirRenderer = class;
  TBlockOpaqueRenderer = class;
  TBlockTranslucentRenderer = class;
  TWorldRenderer = class;
  TWorldChunkRenderer = class;

  { TFPGMapPositionIntegerKey }

  TFPGMapPositionIntegerKey = packed record
    Value: TGPositionInteger;
    class operator = (const Left, Right: TFPGMapPositionIntegerKey): boolean; overload;
    class operator < (const Left, Right: TFPGMapPositionIntegerKey): boolean; overload;
    class operator > (const Left, Right: TFPGMapPositionIntegerKey): boolean; overload;
  end;
  PFPGMapPositionIntegerKey = ^TFPGMapPositionIntegerKey;
function CompareTFPGMapPositionIntegerKey(const PLeft, PRight: PFPGMapPositionIntegerKey): Integer;

type
  { TFPGMapPositionExtendedKey }
  TFPGMapPositionExtendedKey = packed record
    Value: TGPositionExtended;
    class operator = (const Left, Right: TFPGMapPositionExtendedKey): boolean; overload;
    class operator < (const Left, Right: TFPGMapPositionExtendedKey): boolean; overload;
    class operator > (const Left, Right: TFPGMapPositionExtendedKey): boolean; overload;
  end;
  PFPGMapPositionExtendedKey = ^TFPGMapPositionExtendedKey;
function CompareTFPGMapPositionExtendedKey(const PLeft, PRight: PFPGMapPositionExtendedKey): Integer;

type
  { TFPGMapVisibleValue }

  TFPGMapVisibleValue = packed class
    public
      Facings: TSetEnumFacing;
      constructor Create;
  end;
  TFPGMapVisible = specialize TFPGMap<PFPGMapPositionIntegerKey, TFPGMapVisibleValue>;
  TFPGMapWorldChunkRenderer = specialize TFPGMap<PFPGMapPositionExtendedKey, TWorldChunkRenderer>;

  { World }

  { TBlock }

  TBlock = class
    protected
      FRenderer: TBlockRenderer;
    public
      constructor Create(const Renderer: TBlockRenderer = nil);
      procedure SetRenderer(const Renderer: TBlockRenderer);
      property Renderer: TBlockRenderer read FRenderer write SetRenderer;
      function IsAir: boolean; virtual; abstract;
      function IsOpaque: boolean; virtual; abstract;
      destructor Destroy; override;
  end;
  TArrayBlockColumn = specialize TArray<TBlock>;
  TArrayBlockLayer = specialize TArray<TArrayBlockColumn>;
  TArrayBlockCuboid = specialize TArray<TArrayBlockLayer>;

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

  TFunctionWorldForeachBlock = function(Block: TBlock; Position: TGPositionInteger; Arg: Pointer): TBlock;
  TFunctionWorldForeachBlockOfObject = function(Block: TBlock; Position: TGPositionInteger; Arg: Pointer): TBlock of object;
  TFunctionBlockForeachNeighbor = function(BlockTo, BlockFrom: TBlock; PositionTo, PositionFrom: TGPositionInteger; Facing: TEnumFacing; Arg: Pointer): TBlock;
  TFunctionBlockForeachNeighborOfObject = function(BlockTo, BlockFrom: TBlock; PositionTo, PositionFrom: TGPositionInteger; Facing: TEnumFacing; Arg: Pointer): TBlock of object;
  TWorld = class
    protected
      FRenderer: TWorldRenderer;
      FSize: Longint;
    public
      constructor Create(const Size: Longint; const Renderer: TWorldRenderer = nil);
      procedure SetRenderer(const Renderer: TWorldRenderer);
      property Renderer: TWorldRenderer read FRenderer write SetRenderer;
      property Size: Longint read FSize;
      function IsValidPosition(const Position: TGPositionInteger): boolean; virtual;
      function GetBlock(const Position: TGPositionInteger): TBlock; virtual;
      procedure SetBlock(const Position: TGPositionInteger; const Block: TBlock); virtual;
      procedure ForeachBlock(const f: TFunctionWorldForeachBlock; const Concurrent: boolean = false; const Arg: Pointer = nil); virtual; overload;
      procedure ForeachBlock(const f: TFunctionWorldForeachBlockOfObject; const Concurrent: boolean = false; const Arg: Pointer = nil); virtual; overload;
      procedure ForeachBlock(const f: TFunctionWorldForeachBlock; const PositionFrom, PositionTo: TGPositionInteger; const Concurrent: boolean = false; const Arg: Pointer = nil); virtual; overload;
      procedure ForeachBlock(const f: TFunctionWorldForeachBlockOfObject; const PositionFrom, PositionTo: TGPositionInteger; const Concurrent: boolean = false; const Arg: Pointer = nil); virtual; overload;
      procedure ForeachNeighbor(const Position: TGPositionInteger; const f: TFunctionBlockForeachNeighbor; const Arg: Pointer = nil); overload;
      procedure ForeachNeighbor(const Position: TGPositionInteger; const f: TFunctionBlockForeachNeighborOfObject; const Arg: Pointer = nil); overload;
    protected
      Data: TArrayBlockCuboid;
      function InitializeData(Block: TBlock; Position: TGPositionInteger; Arg: Pointer): TBlock; virtual;
    public
      destructor Destroy; override;
  end;

  { Renderer }

  { TCamera }

  TCamera = class
    public
      fovY, ZNear, ZFar: GLdouble;
      constructor Create(const World: TWorld = nil);
      procedure SetWorld(const World: TWorld);
      procedure HandleRotateMouse(const Sender: TOpenGLControl; const Shift: TShiftState; const x, y: Integer);
      procedure HandleRotateKeyboard(const Sender: TOpenGLControl; const TimeDeltaMills: double);
      procedure UpdateRotation;
      procedure Move(const Sender: TOpenGLControl; const TimeDeltaMills: double);
      procedure Render(const Sender: TOpenGLControl);
      function GetPosition: Tvector3_double;
    protected
      FWorld: TWorld;
      FPosition: Tvector3_double;
      Rotation: TQuaternionDouble;
      Front, Left, Up: Tvector3_double;
    public
      property Position: Tvector3_double read GetPosition;
      property World: TWorld read FWorld write SetWorld;
  end;

  { TGLObjects }

  TGLObjects = packed record
    VAO,
    EBO,
    VBOV, VBOC: GLuint;
  end;

  { TGLObjectLists }

  TGLObjectLists = packed record
    EBO: TOpenGLUtilities.TFPGListGLuint;
    VBOV, VBOC: TOpenGLUtilities.TFPGListGLfloat;
  end;

  { TBlockRenderer }

  TBlockRenderer = class
    protected
      FBlock: TBlock;
    public
      constructor Create(const Block: TBlock = nil);
      procedure SetBlock(const Block: TBlock);
      property Block: TBlock read FBlock write SetBlock;
      procedure Render(const Objects: TGLObjectLists; const Position: TGPositionInteger; const Facings: TSetEnumFacing); virtual; abstract;
      destructor Destroy; override;
  end;

  { TBlockRendererDefault }

  TBlockRendererDefault = class(TBlockRenderer)
    public
      procedure Render(const Objects: TGLObjectLists; const Position: TGPositionInteger; const Facings: TSetEnumFacing); override;
      procedure RenderUp(const Objects: TGLObjectLists; const Position: TGPositionInteger); virtual;
      procedure RenderDown(const Objects: TGLObjectLists; const Position: TGPositionInteger); virtual;
      procedure RenderNorth(const Objects: TGLObjectLists; const Position: TGPositionInteger); virtual;
      procedure RenderEast(const Objects: TGLObjectLists; const Position: TGPositionInteger); virtual;
      procedure RenderSouth(const Objects: TGLObjectLists; const Position: TGPositionInteger); virtual;
      procedure RenderWest(const Objects: TGLObjectLists; const Position: TGPositionInteger); virtual;
  end;

  { TBlockAirRenderer }

  TBlockAirRenderer = class(TBlockRendererDefault)
    public
      procedure Render(const Objects: TGLObjectLists; const Position: TGPositionInteger; const Facings: TSetEnumFacing); override;
  end;

  { TBlockOpaqueRenderer }

  TBlockOpaqueRenderer = class(TBlockRendererDefault)
    public
      procedure Render(const Objects: TGLObjectLists; const Position: TGPositionInteger; const Facings: TSetEnumFacing); override;
  end;

  { TBlockTranslucentRenderer }

  TBlockTranslucentRenderer = class(TBlockRendererDefault)
    public
      procedure Render(const Objects: TGLObjectLists; const Position: TGPositionInteger; const Facings: TSetEnumFacing); override;
  end;

  { TWorldRenderer }

  TWorldRenderer = class
    protected
      FWorld: TWorld;
      FChunks: TFPGMapWorldChunkRenderer;
    public
      constructor Create(const World: TWorld = nil);
      procedure SetWorld(const World: TWorld);
      procedure Render; virtual;
      property World: TWorld read FWorld write SetWorld;
      property Chunks: TFPGMapWorldChunkRenderer read FChunks;
      destructor Destroy; override;
  end;

  { TWorldChunkRenderer }

  TWorldChunkRenderer = class
    protected
      FWorld: TWorldRenderer;
      FPositionFrom, FPositionTo: TGPositionInteger;
      RTLCriticalSectionVisible: TRTLCriticalSection;
      RenderInitialized: boolean;
      VisibleOpaque, VisibleTranslucent: TFPGMapVisible;
      GLObjectsOpaque, GLObjectsTranslucent: TGLObjects;
      GLObjectListsOpaque, GLObjectListsTranslucent: TGLObjectLists;
      function InitializeVisible(Block: TBlock; Position: TGPositionInteger; Arg: Pointer): TBlock;
      type TCheckNeighborBlockForVisibleParameters = packed record
        Value: TFPGMapVisibleValue;
      end;
      type PCheckNeighborBlockForVisibleParameters = ^TCheckNeighborBlockForVisibleParameters;
      function CheckNeighborBlockForVisible(BlockTo, BlockFrom: TBlock; PositionTo, PositionFrom: TGPositionInteger; Facing: TEnumFacing; Arg: Pointer): TBlock;
    public
      GLVBOOpaqueValid, GLVBOTranslucentValid: boolean;
      constructor Create(const PositionFrom, PositionTo: TGPositionInteger; const World: TWorldRenderer = nil);
      procedure SetWorldRenderer(const World: TWorldRenderer);
      procedure RenderInitialize; virtual;
      procedure Render; virtual;
      property World: TWorldRenderer read FWorld write SetWorldRenderer;
      property PositionFrom: TGPositionInteger read FPositionFrom;
      property PositionTo: TGPositionInteger read FPositionTo;
      destructor Destroy; override;
  end;

  { Control }

  TKeyRange = 0..$FF;
  TSetKey = set of TKeyRange;

{ UnitGame }

procedure OnIdle0(const Sender: TOpenGLControl; var Done: boolean);
procedure OnResize0(const Sender: TOpenGLControl);
procedure Draw0(const Sender: TOpenGLControl);

{ TApply0Parameters }

type
  TApply0Parameters = packed record
    Size: Longint;
    Sender: TOpenGLControl;
  end;
  PApply0Parameters = ^TApply0Parameters;

{ UnitGame }

procedure Apply1(const Sender: TOpenGLControl; const Size: Longint; const ProgressBarLoading: TProgressBar);
function Apply0(Parameter: Pointer): PtrInt;
procedure Apply0LambdaProgressBar(Data: PtrInt);
procedure OnCreate0(const Sender: TFormMain);
procedure KeyDown0(const Sender: TOpenGLControl; var Key: Word; const Shift: TShiftState);
procedure KeyUp0(const Sender: TOpenGLControl; var Key: Word; const Shift: TShiftState);
procedure OnClick0(const Sender: TOpenGLControl);
procedure OnMouseMove0(const Sender: TOpenGLControl; const Shift: TShiftState; const X, Y: Integer);
procedure OnExit0(const Sender: TOpenGLControl);

procedure OnRendered0(const Sender: TFormMain);
procedure OnTimer0(const Sender: TFormMain);

procedure MouseKeyboardCapture(const Sender: TOpenGLControl);
procedure MouseKeyboardUncapture(const Sender: TOpenGLControl);

{$IFDEF Debug}
type
  THashSetGLenumHash = class
    class function Hash(const a: GLenum; const n: Longint): Longint;
  end;
  THashSetGLenum = specialize THashSet<GLenum, THashSetGLenumHash>;

procedure OnDebugMessage0(Source: GLenum; Type_: GLenum; Id: GLuint; Severity: GLuint; Length: GLsizei; const Message_: PGLchar; UserParam: PGLvoid); extdecl;
{$ENDIF}

const
  { World }
  WorldChunkSize: Integer = 8;
  { Render }
  { Control }
  SetKeyRange: TSetKey = [Low(TKeyRange)..High(TKeyRange)];
  KeysActive: TSetKey = [VK_W, VK_S, VK_A, VK_D, VK_Q, VK_E, VK_SPACE, VK_SHIFT];
  CameraMovementPerMills: double = 10 / MSecsPerSec;
  CameraRotationPerPixel: double = 120 / 800;
  CameraRotationPerMills: double = 180 / MSecsPerSec;
  { Interface }
  ChartFPSCountMax = 1000;
  InterfaceInitializedThreshold = 100;

var
  TimeDeltaMills: double = -1;

implementation

var
  RTLCriticalSectionLoading: TRTLCriticalSection;
  Form: TFormMain;

  RenderControlCenter: TPoint;
  TimeRenderedDay: TDateTime;
  KeysBeingPressed: TSetKey;
  MouseKeyboardCaptured: boolean = false;

  Projection, ModelView: Tmatrix4_double;
  ShaderVertex3D, ShaderFragmentIdentity, ProgramShader: GLhandle;
  AxisX, AxisY, AxisZ: Tvector3_double;

  ICamera: TCamera;
  IWorld: TWorld;
  IWorldRenderer: TWorldRenderer;
  IBlockAir: TBlockAir;
  IBlockAirRenderer: TBlockRenderer;
  IBlockOpaque: TBlock;
  IBlockOpaqueRenderer: TBlockRenderer;
  IBlockTranslucent: TBlock;
  IBlockTranslucentRenderer: TBlockRenderer;

  InterfaceInitialized, FrameNumber: int64;
  FPS, FPSMean, FPSMedian, FPSMax, FPSMin: extended;

  {$IFDEF Debug}
  PreviousWarningTypes: THashSetGLenum;
  {$ENDIF}

{ World }

{ TGPosition }

constructor TGPosition.Create(const x, y, z: T);
begin
  fx:=x;
  fy:=y;
  fz:=z;
end;
constructor TGPosition.Create_Zero;
begin
  Create(0, 0, 0);
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
operator := (const Right: TGPositionInteger): TGPositionExtended;
begin
  Result:=TGPositionExtended.Create(Right.x, Right.y, Right.z);
  Right.Destroy;
end;
operator + (const Left, Right: TGPositionInteger): TGPositionInteger;
begin
  Result:=TGPositionInteger.Create(Left.x + Right.x, Left.y + Right.y, Left.z + Right.z);
  Left.Destroy;
  Right.Destroy;
end;
operator + (const Left, Right: TGPositionExtended): TGPositionExtended;
begin
  Result:=TGPositionExtended.Create(Left.x + Right.x, Left.y + Right.y, Left.z + Right.z);
  Left.Destroy;
  Right.Destroy;
end;
operator / (const Left: TGPositionExtended; const Right: extended): TGPositionExtended;
begin
  Result:=TGPositionExtended.Create(Left.x / Right, Left.y / Right, Left.z / Right);
  Left.Destroy;
end;

{ TFPGMapPositionIntegerKey }

class operator TFPGMapPositionIntegerKey.= (const Left, Right: TFPGMapPositionIntegerKey): boolean;
begin
  Result:=(Left.Value.x = Right.Value.x) and (Left.Value.y = Right.Value.y) and (Left.Value.z = Right.Value.z);
end;
class operator TFPGMapPositionIntegerKey.< (const Left, Right: TFPGMapPositionIntegerKey): boolean;
var
  LeftPosition, RightPosition, CameraPosition: Tvector3_single;
begin
  with Left.Value do LeftPosition.Init(x, y, z);
  with Right.Value do RightPosition.Init(x, y, z);
  CameraPosition:=ICamera.Position;
  Result:=(LeftPosition - CameraPosition).Squared_Length < (RightPosition - CameraPosition).Squared_Length;
end;
class operator TFPGMapPositionIntegerKey.> (const Left, Right: TFPGMapPositionIntegerKey): boolean;
var
  LeftPosition, RightPosition, CameraPosition: Tvector3_single;
begin
  with Left.Value do LeftPosition.Init(x, y, z);
  with Right.Value do RightPosition.Init(x, y, z);
  CameraPosition:=ICamera.Position;
  Result:=(LeftPosition - CameraPosition).Squared_Length > (RightPosition - CameraPosition).Squared_Length;
end;
function CompareTFPGMapPositionIntegerKey(const PLeft, PRight: PFPGMapPositionIntegerKey): Integer;
begin
  if PLeft^ = PRight^ then exit(0)
  else if PLeft^ < PRight^ then exit(1)
  else { if PLeft^ > PRight^ then } exit(-1);
end;

{ TFPGMapPositionExtendedKey }

class operator TFPGMapPositionExtendedKey.= (const Left, Right: TFPGMapPositionExtendedKey): boolean;
begin
  Result:=(Left.Value.x = Right.Value.x) and (Left.Value.y = Right.Value.y) and (Left.Value.z = Right.Value.z);
end;
class operator TFPGMapPositionExtendedKey.< (const Left, Right: TFPGMapPositionExtendedKey): boolean;
var
  LeftPosition, RightPosition, CameraPosition: Tvector3_extended;
begin
  with Left.Value do LeftPosition.Init(x, y, z);
  with Right.Value do RightPosition.Init(x, y, z);
  CameraPosition:=ICamera.Position;
  Result:=(LeftPosition - CameraPosition).Squared_Length < (RightPosition - CameraPosition).Squared_Length;
end;
class operator TFPGMapPositionExtendedKey.> (const Left, Right: TFPGMapPositionExtendedKey): boolean;
var
  LeftPosition, RightPosition, CameraPosition: Tvector3_extended;
begin
  with Left.Value do LeftPosition.Init(x, y, z);
  with Right.Value do RightPosition.Init(x, y, z);
  CameraPosition:=ICamera.Position;
  Result:=(LeftPosition - CameraPosition).Squared_Length > (RightPosition - CameraPosition).Squared_Length;
end;
function CompareTFPGMapPositionExtendedKey(const PLeft, PRight: PFPGMapPositionExtendedKey): Integer;
begin
  if PLeft^ = PRight^ then exit(0)
  else if PLeft^ < PRight^ then exit(1)
  else { if PLeft^ > PRight^ then } exit(-1);
end;

{ TFPGMapVisibleValue }

constructor TFPGMapVisibleValue.Create;
begin
  Facings:=[];
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
  if Renderer <> nil then
  begin
    Renderer.Block:=nil;
    Renderer.Destroy;
  end;
  inherited;
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

constructor TWorld.Create(const Size: Longint; const Renderer: TWorldRenderer = nil);
var
  x, y: Integer;
begin
  FSize:=Size;
  SetLength(Data, Size);
  for x:=0 to Size - 1 do
  begin
    SetLength(Data[x], Size);
    for y:=0 to Size - 1 do
    begin
      SetLength(Data[x][y], Size);
    end;
  end;
  ForeachBlock(@InitializeData, true);
  Self.Renderer:=Renderer;
end;
procedure TWorld.SetRenderer(const Renderer: TWorldRenderer);
begin
  if (Self.Renderer <> nil) and (Renderer <> nil) then raise EAbort.Create(ResStringEIllegal);
  FRenderer:=Renderer;
end;
function TWorld.InitializeData(Block: TBlock; Position: TGPositionInteger; Arg: Pointer): TBlock;
begin
  case Random(3) of
    0: exit(IBlockAir);
    1: exit(IBlockOpaque);
    2: exit(IBlockTranslucent);
    else raise EAbort.Create(ResStringEUnexpected);
  end;
end;
function TWorld.IsValidPosition(const Position: TGPositionInteger): boolean;
begin
  with Position do
  begin
    exit((x >= 0) and (x < Size) and (y >=0) and (y < Size) and (z >= 0) and (z < Size));
  end;
end;
function TWorld.GetBlock(const Position: TGPositionInteger): TBlock;
begin
  if IsValidPosition(Position) then
  begin
    exit(Data[Position.x][Position.y][Position.z]);
  end
  else exit(nil);
end;
procedure TWorld.SetBlock(const Position: TGPositionInteger; const Block: TBlock);
begin
  if Block = nil then exit;
  if IsValidPosition(Position) then
  begin
    Data[Position.x][Position.y][Position.z]:=Block;
  end;
end;
procedure TWorld.ForeachBlock(const f: TFunctionWorldForeachBlock; const Concurrent: boolean = false; const Arg: Pointer = nil);
var
  PositionFrom, PositionTo: TGPositionInteger;
begin
  PositionFrom:=TGPositionInteger.Create_Zero;
  PositionTo:=TGPositionInteger.Create(Size - 1, Size - 1, Size - 1);
  ForeachBlock(f, PositionFrom, PositionTo, Concurrent, Arg);
  PositionFrom.Destroy;
  PositionTo.Destroy;
end;
procedure TWorld.ForeachBlock(const f: TFunctionWorldForeachBlockOfObject; const Concurrent: boolean = false; const Arg: Pointer = nil);
var
  PositionFrom, PositionTo: TGPositionInteger;
begin
  PositionFrom:=TGPositionInteger.Create_Zero;
  PositionTo:=TGPositionInteger.Create(Size - 1, Size - 1, Size - 1);
  ForeachBlock(f, PositionFrom, PositionTo, Concurrent, Arg);
  PositionFrom.Destroy;
  PositionTo.Destroy;
end;
procedure TWorld.ForeachBlock(const f: TFunctionWorldForeachBlock; const PositionFrom, PositionTo: TGPositionInteger; const Concurrent: boolean = false; const Arg: Pointer = nil);
var
  x, DiffX, DiffY, DiffZ, DiffMax: Longint;
  IndexType: TEnumPositionElement = PositionX;
  procedure ForeachBlockLayer(Index: PtrInt; Data: Pointer; Item: TMultiThreadProcItem);
  var
    a, b: Longint;
    Position: TGPositionInteger;
  begin
    case IndexType of
      PositionX:
      begin
        for a:=PositionFrom.y to PositionTo.y do
        begin
          for b:=PositionFrom.z to PositionTo.z do
          begin
            Position:=TGPositionInteger.Create(Index, a, b);
            SetBlock(Position, f(GetBlock(Position), Position, Arg));
            Position.Destroy;
          end;
        end;
      end;
      PositionY:
      begin
        for a:=PositionFrom.x to PositionTo.x do
        begin
          for b:=PositionFrom.z to PositionTo.z do
          begin
            Position:=TGPositionInteger.Create(a, Index, b);
            SetBlock(Position, f(GetBlock(Position), Position, Arg));
            Position.Destroy;
          end;
        end;
      end;
      PositionZ:
      begin
        for a:=PositionFrom.x to PositionTo.x do
        begin
          for b:=PositionFrom.y to PositionTo.y do
          begin
            Position:=TGPositionInteger.Create(a, b, Index);
            SetBlock(Position, f(GetBlock(Position), Position, Arg));
            Position.Destroy;
          end;
        end;
      end;
      else raise EAbort.Create(ResStringEUnexpected);
    end;
  end;
begin
  if Concurrent then
  begin
    DiffX:=PositionTo.x - PositionFrom.x;
    DiffY:=PositionTo.y - PositionFrom.y;
    DiffZ:=PositionTo.z - PositionFrom.z;
    DiffMax:=max(DiffX, max(DiffY, DiffZ));
    if DiffX = DiffMax then IndexType:=PositionX
    else if DiffY = DiffMax then IndexType:=PositionY
    else if DiffZ = DiffMax then IndexType:=PositionZ
    else raise EAbort.Create(ResStringEUnexpected);
    case IndexType of
      PositionX: ProcThreadPool.DoParallelNested(@ForeachBlockLayer, PositionFrom.x, PositionTo.x);
      PositionY: ProcThreadPool.DoParallelNested(@ForeachBlockLayer, PositionFrom.y, PositionTo.y);
      PositionZ: ProcThreadPool.DoParallelNested(@ForeachBlockLayer, PositionFrom.z, PositionTo.z);
      else raise EAbort.Create(ResStringEUnexpected);
    end;
  end
  else
  begin
    for x:=0 to Size - 1 do ForeachBlockLayer(x, nil, nil);
  end;
end;
procedure TWorld.ForeachBlock(const f: TFunctionWorldForeachBlockOfObject; const PositionFrom, PositionTo: TGPositionInteger; const Concurrent: boolean = false; const Arg: Pointer = nil);
var
  x, DiffX, DiffY, DiffZ, DiffMax: Longint;
  IndexType: TEnumPositionElement = PositionX;
  procedure ForeachBlockLayer(Index: PtrInt; Data: Pointer; Item: TMultiThreadProcItem);
  var
    a, b: Longint;
    Position: TGPositionInteger;
  begin
    case IndexType of
      PositionX:
      begin
        for a:=PositionFrom.y to PositionTo.y do
        begin
          for b:=PositionFrom.z to PositionTo.z do
          begin
            Position:=TGPositionInteger.Create(Index, a, b);
            SetBlock(Position, f(GetBlock(Position), Position, Arg));
            Position.Destroy;
          end;
        end;
      end;
      PositionY:
      begin
        for a:=PositionFrom.x to PositionTo.x do
        begin
          for b:=PositionFrom.z to PositionTo.z do
          begin
            Position:=TGPositionInteger.Create(a, Index, b);
            SetBlock(Position, f(GetBlock(Position), Position, Arg));
            Position.Destroy;
          end;
        end;
      end;
      PositionZ:
      begin
        for a:=PositionFrom.x to PositionTo.x do
        begin
          for b:=PositionFrom.y to PositionTo.y do
          begin
            Position:=TGPositionInteger.Create(a, b, Index);
            SetBlock(Position, f(GetBlock(Position), Position, Arg));
            Position.Destroy;
          end;
        end;
      end;
      else raise EAbort.Create(ResStringEUnexpected);
    end;
  end;
begin
  if Concurrent then
  begin
    DiffX:=PositionTo.x - PositionFrom.x;
    DiffY:=PositionTo.y - PositionFrom.y;
    DiffZ:=PositionTo.z - PositionFrom.z;
    DiffMax:=max(DiffX, max(DiffY, DiffZ));
    if DiffX = DiffMax then IndexType:=PositionX
    else if DiffY = DiffMax then IndexType:=PositionY
    else if DiffZ = DiffMax then IndexType:=PositionZ
    else raise EAbort.Create(ResStringEUnexpected);
    case IndexType of
      PositionX: ProcThreadPool.DoParallelNested(@ForeachBlockLayer, PositionFrom.x, PositionTo.x);
      PositionY: ProcThreadPool.DoParallelNested(@ForeachBlockLayer, PositionFrom.y, PositionTo.y);
      PositionZ: ProcThreadPool.DoParallelNested(@ForeachBlockLayer, PositionFrom.z, PositionTo.z);
      else raise EAbort.Create(ResStringEUnexpected);
    end;
  end
  else
  begin
    for x:=0 to Size - 1 do ForeachBlockLayer(x, nil, nil);
  end;
end;
procedure TWorld.ForeachNeighbor(const Position: TGPositionInteger; const f: TFunctionBlockForeachNeighbor; const Arg: Pointer = nil);
var
  BlockFrom: TBlock;
  Facing: TEnumFacing;
  PositionTo: TGPositionInteger;
begin
  BlockFrom:=GetBlock(Position);
  for Facing in TEnumFacing do
  begin
    PositionTo:=Position.Offset(Facing);
    SetBlock(PositionTo, f(GetBlock(PositionTo), BlockFrom, PositionTo, Position, Facing, Arg));
    PositionTo.Destroy;
  end;
end;
procedure TWorld.ForeachNeighbor(const Position: TGPositionInteger; const f: TFunctionBlockForeachNeighborOfObject; const Arg: Pointer = nil);
var
  BlockFrom: TBlock;
  Facing: TEnumFacing;
  PositionTo: TGPositionInteger;
begin
  BlockFrom:=GetBlock(Position);
  for Facing in TEnumFacing do
  begin
    PositionTo:=Position.Offset(Facing);
    SetBlock(PositionTo, f(GetBlock(PositionTo), BlockFrom, PositionTo, Position, Facing, Arg));
    PositionTo.Destroy;
  end;
end;
destructor TWorld.Destroy;
begin
  if Renderer <> nil then
  begin
    Renderer.World:=nil;
    Renderer.Destroy;
  end;
  inherited;
end;

{ Renderer }

{ TCamera }

constructor TCamera.Create(const World: TWorld = nil);
begin
  fovY:=60; // 90 not allowed.
  ZNear:=0.1;
  ZFar:=1000;

  Rotation.Init_AxisAngle(AxisX, 0);
  Front.Init_Zero;
  Front:=AxisX;
  Left.Init_Zero;
  Left:=AxisY;
  Up.Init_Zero;
  Up:=AxisZ;

  Self.World:=World;
end;
procedure TCamera.SetWorld(const World: TWorld);
var
  WorldCenter: double;
begin
  if (Self.World <> nil) and (World <> nil) then raise EAbort.Create(ResStringEIllegal);
  FWorld:=World;
  if Self.World <> nil then
  begin
    WorldCenter:=(0 + Self.World.Size) / 2;
    FPosition.Init(WorldCenter, WorldCenter, Self.World.Size + 1);
  end;
end;
function TCamera.GetPosition: Tvector3_double;
var
  Copy: Tvector3_double;
begin
  Copy:=FPosition; // Copy
  exit(Copy);
end;
procedure TCamera.HandleRotateMouse(const Sender: TOpenGLControl; const Shift: TShiftState; const x, y: Integer);
var
  QYaw, QPitch: TQuaternionDouble;
begin
  QYaw.Init_AxisAngle(Up, -CameraRotationPerPixel * (x - RenderControlCenter.x));
  QPitch.Init_AxisAngle(Left, CameraRotationPerPixel * (y - RenderControlCenter.y));
  Rotation:=(QYaw * (QPitch * Rotation).Normalize).Normalize;
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
  QRoll.Init_AxisAngle(Front, RollDiff);
  Rotation:=(QRoll * Rotation).Normalize;
end;
procedure TCamera.UpdateRotation;
begin
  with TMatrixUtilities do
  begin
    Normalize(Front, Rotation * AxisX);
    Normalize(Left, Rotation * AxisY);
    Normalize(Up, Rotation * AxisZ);
  end;
end;
procedure TCamera.Move(const Sender: TOpenGLControl; const TimeDeltaMills: double);
var
  CameraMovement: double;
  PositionPrev: Tvector3_double;
  i: Integer;
begin
  CameraMovement:=CameraMovementPerMills * TimeDeltaMills;
  PositionPrev:=Position;
  if VK_W in KeysBeingPressed then FPosition:=Position + Front * CameraMovement;
  if VK_S in KeysBeingPressed then FPosition:=Position - Front * CameraMovement;
  if VK_A in KeysBeingPressed then FPosition:=Position + Left * CameraMovement;
  if VK_D in KeysBeingPressed then FPosition:=Position - Left * CameraMovement;
  if VK_SPACE in KeysBeingPressed then FPosition:=Position + Up * CameraMovement;
  if VK_SHIFT in KeysBeingPressed then FPosition:=Position - Up * CameraMovement;
  if not (Position = PositionPrev) then
  begin
    with World.Renderer.Chunks do
    begin
      for i:=0 to Count - 1 do Data[i].GLVBOTranslucentValid:=false;
    end;
  end;
end;
procedure TCamera.Render(const Sender: TOpenGLControl);
var
  ProjectionS, ModelViewS: Tmatrix4_single;
begin
  Projection.Init_Identity;
  with Sender do TOpenGLUtilities.Perspectived2(Projection, fovY, Width / Height, ZNear, ZFar);
  ProjectionS:=Projection;
  glUniformMatrix4fv(glGetUniformLocation(ProgramShader, OGLShaderVertex3DUniformProjectionMat), 1, GL_FALSE, @ProjectionS.Data);

  ModelView.Init_Identity;
  TOpenGLUtilities.LookAtd2(ModelView, Position, Position + Front, Up);
  ModelViewS:=ModelView;
  glUniformMatrix4fv(glGetUniformLocation(ProgramShader, OGLShaderVertex3DUniformModelViewMat), 1, GL_FALSE, @ModelViewS.Data);
end;

{ TBlockRenderer }

constructor TBlockRenderer.Create(const Block: TBlock = nil);
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
  if Block <> nil then
  begin
    Block.Renderer:=nil;
    Block.Destroy;
  end;
  inherited;
end;

{ TBlockRendererDefault }

procedure TBlockRendererDefault.Render(const Objects: TGLObjectLists; const Position: TGPositionInteger; const Facings: TSetEnumFacing);
begin
  if FacingUp in Facings then RenderUp(Objects, Position);
  if FacingDown in Facings then RenderDown(Objects, Position);
  if FacingNorth in Facings then RenderNorth(Objects, Position);
  if FacingEast in Facings then RenderEast(Objects, Position);
  if FacingSouth in Facings then RenderSouth(Objects, Position);
  if FacingWest in Facings then RenderWest(Objects, Position);
end;
procedure TBlockRendererDefault.RenderUp(const Objects: TGLObjectLists; const Position: TGPositionInteger);
var
  EBOOffset: Integer;
begin
  with Objects do
  begin
    with VBOV do
    begin
      EBOOffset:=Count div 4;
      with Position do
      begin
            Add(x);    Add(y);Add(z + 1);Add(1);
        Add(x + 1);    Add(y);Add(z + 1);Add(1);
        Add(x + 1);Add(y + 1);Add(z + 1);Add(1);
            Add(x);Add(y + 1);Add(z + 1);Add(1);
      end;
    end;
    with EBO do
    begin
      Add(EBOOffset + 0);Add(EBOOffset + 1);Add(EBOOffset + 2);
      Add(EBOOffset + 2);Add(EBOOffset + 3);Add(EBOOffset + 0);
    end;
  end;
end;
procedure TBlockRendererDefault.RenderDown(const Objects: TGLObjectLists; const Position: TGPositionInteger);
var
  EBOOffset: Integer;
begin
  with Objects do
  begin
    with VBOV do
    begin
      EBOOffset:=Count div 4;
      with Position do
      begin
            Add(x);    Add(y);Add(z);Add(1);
            Add(x);Add(y + 1);Add(z);Add(1);
        Add(x + 1);Add(y + 1);Add(z);Add(1);
        Add(x + 1);    Add(y);Add(z);Add(1);
      end;
    end;
    with EBO do
    begin
      Add(EBOOffset + 0);Add(EBOOffset + 1);Add(EBOOffset + 2);
      Add(EBOOffset + 2);Add(EBOOffset + 3);Add(EBOOffset + 0);
    end;
  end;
end;
procedure TBlockRendererDefault.RenderNorth(const Objects: TGLObjectLists; const Position: TGPositionInteger);
var
  EBOOffset: Integer;
begin
  with Objects do
  begin
    with VBOV do
    begin
      EBOOffset:=Count div 4;
      with Position do
      begin
        Add(x + 1);    Add(y);    Add(z);Add(1);
        Add(x + 1);Add(y + 1);    Add(z);Add(1);
        Add(x + 1);Add(y + 1);Add(z + 1);Add(1);
        Add(x + 1);    Add(y);Add(z + 1);Add(1);
      end;
        end;
    with EBO do
    begin
      Add(EBOOffset + 0);Add(EBOOffset + 1);Add(EBOOffset + 2);
      Add(EBOOffset + 2);Add(EBOOffset + 3);Add(EBOOffset + 0);
    end;
  end;
end;
procedure TBlockRendererDefault.RenderEast(const Objects: TGLObjectLists; const Position: TGPositionInteger);
var
  EBOOffset: Integer;
begin
  with Objects do
  begin
    with VBOV do
    begin
      EBOOffset:=Count div 4;
      with Position do
      begin
            Add(x);Add(y);    Add(z);Add(1);
        Add(x + 1);Add(y);    Add(z);Add(1);
        Add(x + 1);Add(y);Add(z + 1);Add(1);
            Add(x);Add(y);Add(z + 1);Add(1);
      end;
    end;
    with EBO do
    begin
      Add(EBOOffset + 0);Add(EBOOffset + 1);Add(EBOOffset + 2);
      Add(EBOOffset + 2);Add(EBOOffset + 3);Add(EBOOffset + 0);
    end;
  end;
end;
procedure TBlockRendererDefault.RenderSouth(const Objects: TGLObjectLists; const Position: TGPositionInteger);
var
  EBOOffset: Integer;
begin
  with Objects do
  begin
    with VBOV do
    begin
      EBOOffset:=Count div 4;
      with Position do
      begin
        Add(x);    Add(y);    Add(z);Add(1);
        Add(x);    Add(y);Add(z + 1);Add(1);
        Add(x);Add(y + 1);Add(z + 1);Add(1);
        Add(x);Add(y + 1);    Add(z);Add(1);
      end;
    end;
    with EBO do
    begin
      Add(EBOOffset + 0);Add(EBOOffset + 1);Add(EBOOffset + 2);
      Add(EBOOffset + 2);Add(EBOOffset + 3);Add(EBOOffset + 0);
    end;
    end;
end;
procedure TBlockRendererDefault.RenderWest(const Objects: TGLObjectLists; const Position: TGPositionInteger);
var
  EBOOffset: Integer;
begin
  with Objects do
  begin
    with VBOV do
    begin
      EBOOffset:=Count div 4;
      with Position do
      begin
            Add(x);Add(y + 1);    Add(z);Add(1);
            Add(x);Add(y + 1);Add(z + 1);Add(1);
        Add(x + 1);Add(y + 1);Add(z + 1);Add(1);
        Add(x + 1);Add(y + 1);    Add(z);Add(1);
      end;
    end;
    with EBO do
    begin
      Add(EBOOffset + 0);Add(EBOOffset + 1);Add(EBOOffset + 2);
      Add(EBOOffset + 2);Add(EBOOffset + 3);Add(EBOOffset + 0);
    end;
  end;
end;

{ TBlockAirRenderer }

procedure TBlockAirRenderer.Render(const Objects: TGLObjectLists; const Position: TGPositionInteger; const Facings: TSetEnumFacing);
begin
  // NOOP
end;

{ TBlockOpaqueRenderer }

procedure TBlockOpaqueRenderer.Render(const Objects: TGLObjectLists; const Position: TGPositionInteger; const Facings: TSetEnumFacing);
var
  R, G, B: Extended;
  Facing: TEnumFacing;
begin
  R:=Random;
  G:=Random;
  B:=Random;
  for Facing in TEnumFacing do
  begin
    if Facing in Facings then
    begin
      with Objects.VBOC do
      begin
        Add(R);Add(G);Add(B);Add(1);
        Add(R);Add(G);Add(B);Add(1);
        Add(R);Add(G);Add(B);Add(1);
        Add(R);Add(G);Add(B);Add(1);
      end;
    end;
  end;
  inherited;
end;

{ TBlockTranslucentRenderer }

procedure TBlockTranslucentRenderer.Render(const Objects: TGLObjectLists; const Position: TGPositionInteger; const Facings: TSetEnumFacing);
var
  R, G, B, A: Extended;
  Facing: TEnumFacing;
begin
  R:=Random;
  G:=Random;
  B:=Random;
  A:=Random;
  for Facing in TEnumFacing do
  begin
    if Facing in Facings then
    begin
      with Objects.VBOC do
      begin
        Add(R);Add(G);Add(B);Add(A);
        Add(R);Add(G);Add(B);Add(A);
        Add(R);Add(G);Add(B);Add(A);
        Add(R);Add(G);Add(B);Add(A);
      end;
    end;
  end;
  inherited;
end;

{ TWorldRenderer }

constructor TWorldRenderer.Create(const World: TWorld = nil);
begin
  FChunks:=TFPGMapWorldChunkRenderer.Create;
  Chunks.OnKeyCompare:=@CompareTFPGMapPositionExtendedKey;
  Self.World:=World;
end;
procedure TWorldRenderer.SetWorld(const World: TWorld);
var
  x, y, z: Longint;
  CoordMax: Longint;
  PositionCenterOffset: TGPositionExtended;
  PositionFrom, PositionTo: TGPositionInteger;
  PKey: PFPGMapPositionExtendedKey;
begin
  PositionCenterOffset:=TGPositionExtended.Create(0.5, 0.5, 0.5);
  if (Self.World <> nil) and (World <> nil) then raise EAbort.Create(ResStringEIllegal);
  FWorld:=World;
  if Self.World <> nil then
  begin
    CoordMax:=World.Size - 1;
    x:=0;
    while x < World.Size do
    begin
      y:=0;
      while y < World.Size do
      begin
        z:=0;
        while z < World.Size do
        begin
          PositionFrom:=TGPositionInteger.Create(x, y, z);
          PositionTo:=TGPositionInteger.Create(min(x + WorldChunkSize - 1, CoordMax), min(y + WorldChunkSize - 1, CoordMax), min(z + WorldChunkSize - 1, CoordMax));
          New(PKey);
          PKey^.Value:=(PositionFrom.Clone + PositionTo.Clone) / 2 + PositionCenterOffset.Clone;
          Chunks.Add(PKey,
                     TWorldChunkRenderer.Create(PositionFrom, PositionTo, Self));
          Inc(z, WorldChunkSize);
        end;
        Inc(y, WorldChunkSize);
      end;
      Inc(x, WorldChunkSize);
    end;
  end;
  PositionCenterOffset.Destroy;
end;
procedure TWorldRenderer.Render;
var
  i: Integer;
  Chunk: TWorldChunkRenderer;
begin
  glEnable(GL_CULL_FACE);
  glEnable(GL_DEPTH_TEST);
  glEnable(GL_BLEND);
  glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);

  Chunks.Sort;
  with Chunks do
  begin
    for i:=0 to Count - 1 do
    begin
      Chunk:=Data[i];
      if not Chunk.RenderInitialized then
      begin
        Chunk.RenderInitialize;
        Chunk.RenderInitialized:=true;
      end;
      Chunk.Render;
    end;
  end;

  glDisable(GL_BLEND);
  glDisable(GL_DEPTH_TEST);
  glDisable(GL_CULL_FACE);
end;
destructor TWorldRenderer.Destroy;
var
  i: Integer;
  PKeyE: PFPGMapPositionExtendedKey;
  Chunk: TWorldChunkRenderer;
begin
  with Chunks do
  begin
    for i:=0 to Count - 1 do
    begin
      PKeyE:=Keys[i];
      Chunk:=Data[i];
      PKeyE^.Value.Destroy;
      Dispose(PKeyE);
      Chunk.World:=nil;
      Chunk.Destroy;
    end;
  end;
  Chunks.Destroy;

  if World <> nil then
  begin
    World.Renderer:=nil;
    World.Destroy;
  end;
  inherited;
end;

{ TWorldChunkRenderer }

constructor TWorldChunkRenderer.Create(const PositionFrom, PositionTo: TGPositionInteger; const World: TWorldRenderer = nil);
begin
  InitCriticalSection(RTLCriticalSectionVisible);

  FPositionFrom:=PositionFrom;
  FPositionTo:=PositionTo;

  VisibleOpaque:=TFPGMapVisible.Create;
  VisibleOpaque.OnKeyCompare:=@CompareTFPGMapPositionIntegerKey;
  VisibleTranslucent:=TFPGMapVisible.Create;
  VisibleTranslucent.OnKeyCompare:=@CompareTFPGMapPositionIntegerKey;

  RenderInitialized:=false;
  GLVBOOpaqueValid:=false;
  GLVBOTranslucentValid:=false;
  Self.World:=World;
end;
procedure TWorldChunkRenderer.SetWorldRenderer(const World: TWorldRenderer);
begin
  if (Self.World <> nil) and (World <> nil) then raise EAbort.Create(ResStringEIllegal);
  FWorld:=World;
  if Self.World <> nil then Self.World.World.ForeachBlock(@InitializeVisible, PositionFrom, PositionTo, true);
end;
function TWorldChunkRenderer.InitializeVisible(Block: TBlock; Position: TGPositionInteger; Arg: Pointer): TBlock;
var
  Parameters: TCheckNeighborBlockForVisibleParameters;
  Visible: TFPGMapVisible;
  PKey: PFPGMapPositionIntegerKey;
begin
  Parameters.Value:=TFPGMapVisibleValue.Create;
  World.World.ForeachNeighbor(Position, @CheckNeighborBlockForVisible, @Parameters);

  if Parameters.Value.Facings = [] then Parameters.Value.Destroy
  else
  begin
    if Block.IsOpaque then Visible:=VisibleOpaque
    else Visible:=VisibleTranslucent;
    New(PKey);
    PKey^.Value:=Position.Clone;
    EnterCriticalSection(RTLCriticalSectionVisible);
    Visible.Add(PKey, Parameters.Value);
    LeaveCriticalSection(RTLCriticalSectionVisible);
  end;

  exit(Block);
end;
procedure TWorldChunkRenderer.RenderInitialize;
begin
  with GLObjectListsOpaque do
  begin
    EBO:=TOpenGLUtilities.TFPGListGLuint.Create;
    VBOV:=TOpenGLUtilities.TFPGListGLfloat.Create;
    VBOC:=TOpenGLUtilities.TFPGListGLfloat.Create;
  end;

  with GLObjectListsTranslucent do
  begin
    EBO:=TOpenGLUtilities.TFPGListGLuint.Create;
    VBOV:=TOpenGLUtilities.TFPGListGLfloat.Create;
    VBOC:=TOpenGLUtilities.TFPGListGLfloat.Create;
  end;

  with GLObjectsOpaque do
  begin
    glGenVertexArrays(1, @VAO);
    glGenBuffers(1, @EBO);
    glGenBuffers(1, @VBOV);
    glGenBuffers(1, @VBOC);

    glBindVertexArray(VAO);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);

    glBindBuffer(GL_ARRAY_BUFFER, VBOV);
    glVertexAttribPointer(0, 4, GL_FLOAT, GL_FALSE, SizeOf(GLfloat) * 4, PointerNil);
    glEnableVertexAttribArray(0);

    glBindBuffer(GL_ARRAY_BUFFER, VBOC);
    glVertexAttribPointer(1, 4, GL_FLOAT, GL_FALSE, SizeOf(GLfloat) * 4, PointerNil);
    glEnableVertexAttribArray(1);

    glBindVertexArray(0);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0);
    glBindBuffer(GL_ARRAY_BUFFER, 0);

    {$IFDEF Debug}
    with TOpenGLUtilities do
    begin
      glBindVertexArray(VAO);
      ObjectLabel(GL_VERTEX_ARRAY, VAO, ResStringOGLObjLabelChunkOpaqueVAO);
      ObjectLabel(GL_BUFFER, EBO, ResStringOGLObjLabelChunkOpaqueEBO);
      ObjectLabel(GL_BUFFER, VBOV, ResStringOGLObjLabelChunkOpaqueVBOV);
      ObjectLabel(GL_BUFFER, VBOC, ResStringOGLObjLabelChunkOpaqueVBOC);
    end;
    {$ENDIF}
  end;

  with GLObjectsTranslucent do
  begin
    glGenVertexArrays(1, @VAO);
    glGenBuffers(1, @EBO);
    glGenBuffers(1, @VBOV);
    glGenBuffers(1, @VBOC);

    glBindVertexArray(VAO);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);

    glBindBuffer(GL_ARRAY_BUFFER, VBOV);
    glVertexAttribPointer(0, 4, GL_FLOAT, GL_FALSE, SizeOf(GLfloat) * 4, PointerNil);
    glEnableVertexAttribArray(0);

    glBindBuffer(GL_ARRAY_BUFFER, VBOC);
    glVertexAttribPointer(1, 4, GL_FLOAT, GL_FALSE, SizeOf(GLfloat) * 4, PointerNil);
    glEnableVertexAttribArray(1);

    glBindVertexArray(0);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0);
    glBindBuffer(GL_ARRAY_BUFFER, 0);

    {$IFDEF Debug}
    with TOpenGLUtilities do
    begin
      ObjectLabel(GL_VERTEX_ARRAY, VAO, ResStringOGLObjLabelChunkTranslucentVAO);
      ObjectLabel(GL_BUFFER, EBO, ResStringOGLObjLabelChunkTranslucentEBO);
      ObjectLabel(GL_BUFFER, VBOV, ResStringOGLObjLabelChunkTranslucentVBOV);
      ObjectLabel(GL_BUFFER, VBOC, ResStringOGLObjLabelChunkTranslucentVBOC);
    end;
    {$ENDIF}
  end;
end;
function TWorldChunkRenderer.CheckNeighborBlockForVisible(BlockTo, BlockFrom: TBlock; PositionTo, PositionFrom: TGPositionInteger; Facing: TEnumFacing; Arg: Pointer): TBlock;
var
  PParameters: PCheckNeighborBlockForVisibleParameters;
begin
  if (BlockTo = nil) or (not BlockTo.IsOpaque) then
  begin
    PParameters:=PCheckNeighborBlockForVisibleParameters(Arg);
    Include(PParameters^.Value.Facings, Facing);
  end;
  exit(BlockTo);
end;
procedure TWorldChunkRenderer.Render;
var
  i: Integer;
  PKeyI: PFPGMapPositionIntegerKey;
  PDataGLfloat: TOpenGLUtilities.PFPGListArrayGLfloat;
  PDataGLuint: TOpenGLUtilities.PFPGListArrayGLuint;
begin
  if not GLVBOOpaqueValid then
  begin
    with GLObjectListsOpaque do
    begin
      EBO.Clear;
      VBOV.Clear;
      VBOC.Clear;
    end;
    with VisibleOpaque do
    begin
      for i:=0 to Count - 1 do
      begin
        PKeyI:=Keys[i];
        World.World.GetBlock(PKeyI^.Value).Renderer.Render(GLObjectListsOpaque, PKeyI^.Value, Data[i].Facings);
      end;
    end;
    with GLObjectsOpaque do
    begin
      glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
      PDataGLuint:=GLObjectListsOpaque.EBO.List;
      glBufferData(GL_ELEMENT_ARRAY_BUFFER, SizeOf(GLuint) * GLObjectListsOpaque.EBO.Count, PDataGLuint, GL_STATIC_DRAW);

      glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0);

      glBindBuffer(GL_ARRAY_BUFFER, VBOV);
      PDataGLfloat:=GLObjectListsOpaque.VBOV.List;
      glBufferData(GL_ARRAY_BUFFER, SizeOf(GLfloat) * GLObjectListsOpaque.VBOV.Count, PDataGLfloat, GL_STATIC_DRAW);

      glBindBuffer(GL_ARRAY_BUFFER, VBOC);
      PDataGLfloat:=GLObjectListsOpaque.VBOC.List;
      glBufferData(GL_ARRAY_BUFFER, SizeOf(GLfloat) * GLObjectListsOpaque.VBOC.Count, PDataGLfloat, GL_STATIC_DRAW);

      glBindBuffer(GL_ARRAY_BUFFER, 0);
    end;
    GLVBOOpaqueValid:=true;
  end;
  with GLObjectsOpaque do
  begin
    glBindVertexArray(VAO);
    glBindBuffer(GL_ARRAY_BUFFER, VBOV);
    glDrawElements(GL_TRIANGLES, GLObjectListsOpaque.EBO.Count, GL_UNSIGNED_INT, PointerNil);
    glBindBuffer(GL_ARRAY_BUFFER, VBOC);
    glDrawElements(GL_TRIANGLES, GLObjectListsOpaque.EBO.Count, GL_UNSIGNED_INT, PointerNil);
    glBindVertexArray(0);
  end;

  if not GLVBOTranslucentValid then
  begin
    with GLObjectListsTranslucent do
    begin
      EBO.Clear;
      VBOV.Clear;
      VBOC.Clear;
    end;
    VisibleTranslucent.Sort;
    with VisibleTranslucent do
    begin
      for i:=0 to Count - 1 do
      begin
        PKeyI:=Keys[i];
        World.World.GetBlock(PKeyI^.Value).Renderer.Render(GLObjectListsTranslucent, PKeyI^.Value, Data[i].Facings);
      end;
    end;
    with GLObjectsTranslucent do
    begin
      glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
      PDataGLuint:=GLObjectListsTranslucent.EBO.List;
      glBufferData(GL_ELEMENT_ARRAY_BUFFER, SizeOf(GLuint) * GLObjectListsTranslucent.EBO.Count, PDataGLuint, GL_STREAM_DRAW);

      glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0);

      glBindBuffer(GL_ARRAY_BUFFER, VBOV);
      PDataGLfloat:=GLObjectListsTranslucent.VBOV.List;
      glBufferData(GL_ARRAY_BUFFER, SizeOf(GLfloat) * GLObjectListsTranslucent.VBOV.Count, PDataGLfloat, GL_STREAM_DRAW);

      glBindBuffer(GL_ARRAY_BUFFER, VBOC);
      PDataGLfloat:=GLObjectListsTranslucent.VBOC.List;
      glBufferData(GL_ARRAY_BUFFER, SizeOf(GLfloat) * GLObjectListsTranslucent.VBOC.Count, PDataGLfloat, GL_STREAM_DRAW);

      glBindBuffer(GL_ARRAY_BUFFER, 0);
    end;
    GLVBOTranslucentValid:=true;
  end;
  with GLObjectsTranslucent do
  begin
    glBindVertexArray(VAO);
    glBindBuffer(GL_ARRAY_BUFFER, VBOV);
    glDrawElements(GL_TRIANGLES, GLObjectListsTranslucent.EBO.Count, GL_UNSIGNED_INT, PointerNil);
    glBindBuffer(GL_ARRAY_BUFFER, VBOC);
    glDrawElements(GL_TRIANGLES, GLObjectListsTranslucent.EBO.Count, GL_UNSIGNED_INT, PointerNil);
    glBindVertexArray(0);
  end;
end;
destructor TWorldChunkRenderer.Destroy;
var
  i: Integer;
  PKeyI: PFPGMapPositionIntegerKey;
  PKeyE: PFPGMapPositionExtendedKey;
begin
  with VisibleOpaque do
  begin
    for i:=0 to Count - 1 do
    begin
      PKeyI:=Keys[i];
      Data[i].Destroy;
      PKeyI^.Value.Destroy;
      Dispose(PKeyI);
    end;
  end;
  VisibleOpaque.Destroy;
  with VisibleTranslucent do
  begin
    for i:=0 to Count - 1 do
    begin
      PKeyI:=Keys[i];
      Data[i].Destroy;
      PKeyI^.Value.Destroy;
      Dispose(PKeyI);
    end;
  end;
  VisibleTranslucent.Destroy;

  with GLObjectListsOpaque do
  begin
    EBO.Destroy;
    VBOV.Destroy;
    VBOC.Destroy;
  end;

  with GLObjectListsTranslucent do
  begin
    EBO.Destroy;
    VBOV.Destroy;
    VBOC.Destroy;
  end;

  with GLObjectsOpaque do
  begin
    glDeleteVertexArrays(1, @VAO);
    glDeleteBuffers(1, @EBO);
    glDeleteBuffers(1, @VBOV);
    glDeleteBuffers(1, @VBOC);
  end;

  with GLObjectsTranslucent do
  begin
    glDeleteVertexArrays(1, @VAO);
    glDeleteBuffers(1, @EBO);
    glDeleteBuffers(1, @VBOV);
    glDeleteBuffers(1, @VBOC);
  end;

  PositionFrom.Destroy;
  FPositionTo.Destroy;

  DoneCriticalSection(RTLCriticalSectionVisible);

  if World <> nil then
  begin
    with World.Chunks do
    begin
      PKeyE:=Keys[IndexOfData(Self)];
      Remove(PKeyE);
      Dispose(PKeyE);
    end;
    World.Destroy;
  end;
  inherited;
end;

{ UnitGame }

{ Render }

procedure OnIdle0(const Sender: TOpenGLControl; var Done: boolean);
{ var
  Key: word; }
begin
  Done:=true;
  Sender.Invalidate;
  { for Key in KeysBeingPressed do
  begin
    if Key in KeysActive then
    begin
      Sender.Invalidate;
      break;
    end;
  end; }
end;
procedure OnResize0(const Sender: TOpenGLControl);
begin
  with RenderControlCenter do
  begin
    with Sender do
    begin
      x:=Width div 2;
      y:=Height div 2;
    end;
  end;
end;
procedure Draw0(const Sender: TOpenGLControl);
begin
  if not (TryEnterCriticalsection(RTLCriticalSectionLoading) = 0) then
  begin
    TimeDeltaMills:=MSecsPerDay * (Now - TimeRenderedDay);
    TimeRenderedDay:=Now;

    glClearColor(0.52, 0.80, 0.92, 1.0); // Sky
    glClear(GL_COLOR_BUFFER_BIT or GL_DEPTH_BUFFER_BIT);
    glUseProgram(ProgramShader);
    with ICamera do
    begin
      HandleRotateKeyboard(Sender, TimeDeltaMills);
      UpdateRotation;
      Move(Sender, TimeDeltaMills);
      Render(Sender);
    end;
    IWorldRenderer.Render;
    Sender.SwapBuffers;

    OnRendered0(Form);

    LeaveCriticalSection(RTLCriticalSectionLoading);
  end;
end;

{ Control }

procedure Apply1(const Sender: TOpenGLControl; const Size: Longint; const ProgressBarLoading: TProgressBar);
var
  PParameters: PApply0Parameters;
begin
  Form.ProgressBarLoading.Position:=0;
  Form.ProgressBarLoading.Visible:=true;

  New(PParameters);
  PParameters^.Sender:=Sender;
  PParameters^.Size:=Size;
  BeginThread(@Apply0, PParameters);
end;
function Apply0(Parameter: Pointer): PtrInt;
var
  PParameters: PApply0Parameters;
  LambdaProgressBar: TProcedurePointer;
begin
  PParameters:=PApply0Parameters(Parameter);
  LambdaProgressBar:=TProcedurePointer.Create(@Apply0LambdaProgressBar);

  EnterCriticalSection(RTLCriticalSectionLoading);
  InterfaceInitialized:=0;
  ICamera.Free;
  TThread.Queue(nil, @IWorld.Free); // GL memory leak if not so
  Application.QueueAsyncCall(@LambdaProgressBar.Run, 10);

  ICamera:=TCamera.Create;
  IWorldRenderer:=TWorldRenderer.Create;
  Application.QueueAsyncCall(@LambdaProgressBar.Run, 30);

  IWorld:=TWorld.Create(PParameters^.Size, IWorldRenderer);
  Application.QueueAsyncCall(@LambdaProgressBar.Run, 50);

  ICamera.World:=IWorld;
  IWorldRenderer.World:=IWorld;
  TThread.Synchronize(nil, @ThreadUtilities.AwaitSynchornize);
  Application.QueueAsyncCall(@LambdaProgressBar.Run, 90);

  TimeRenderedDay:=Now;
  LeaveCriticalSection(RTLCriticalSectionLoading);

  Application.QueueAsyncCall(@LambdaProgressBar.Run, 100);
  Application.QueueAsyncCall(@LambdaProgressBar.Destroy, 0);
  TThread.Queue(nil, @PParameters^.Sender.Invalidate);
  Dispose(PParameters);
  EndThread;
  exit(0);
end;
procedure Apply0LambdaProgressBar(Data: PtrInt);
begin
  Form.ProgressBarLoading.Position:=Data;
end;
procedure OnCreate0(const Sender: TFormMain);
begin
  Form:=Sender;

  {$IFDEF Debug}
  glEnable(GL_DEBUG_OUTPUT);
  {$IFDEF OpenGLDebugSync}glEnable(GL_DEBUG_OUTPUT_SYNCHRONOUS);{$ENDIF}
  glDebugMessageCallback(@OnDebugMessage0, Pointer(0));
  {$ENDIF}

  ShaderVertex3D:=CompileShader(LoadShaderFromResourceName(OGLShaderVertex3D), GL_VERTEX_SHADER);
  ShaderFragmentIdentity:=CompileShader(LoadShaderFromResourceName(OGLShaderFragementIdentity), GL_FRAGMENT_SHADER);
  ProgramShader:=LinkProgram(TArrayShader.Create(ShaderVertex3D, ShaderFragmentIdentity));

  {$IFDEF Debug}
  with TOpenGLUtilities do
  begin
    ObjectLabel(GL_SHADER, ShaderVertex3D, ResStringOGLObjLabelShaderVertex);
    ObjectLabel(GL_SHADER, ShaderFragmentIdentity, ResStringOGLObjLabelShaderFragment);
    ObjectLabel(GL_PROGRAM, ProgramShader, ResStringOGLObjLabelProgramShader);
  end;
  {$ENDIF}
end;
procedure KeyDown0(const Sender: TOpenGLControl; var Key: word; const Shift: TShiftState);
begin
  case Key of
    VK_ESCAPE: MouseKeyboardUncapture(Sender);
  end;
  if not (Key in SetKeyRange) then exit;
  Sender.Repaint;
  Include(KeysBeingPressed, Key);
end;
procedure KeyUp0(const Sender: TOpenGLControl; var Key: word; const Shift: TShiftState);
begin
  if not (Key in SetKeyRange) then exit;
  Exclude(KeysBeingPressed, Key);
end;
procedure OnMouseMove0(const Sender: TOpenGLControl; const Shift: TShiftState; const x, y: Integer);
begin
  if MouseKeyboardCaptured then ICamera.HandleRotateMouse(Sender, Shift, x, y);
end;
procedure OnClick0(const Sender: TOpenGLControl);
begin
  if not MouseKeyboardCaptured then MouseKeyboardCapture(Sender);
end;
procedure OnExit0(const Sender: TOpenGLControl);
begin
  if MouseKeyboardCaptured then MouseKeyboardUncapture(Sender);
end;

{ Interface }

procedure OnRendered0(const Sender: TFormMain);
begin
  if InterfaceInitialized < InterfaceInitializedThreshold then
  begin
    if InterfaceInitialized = 0 then
    begin
      FrameNumber:=0;
      FPS:=MSecsPerSec / TimeDeltaMills;
      FPSMean:=FPS;
      FPSMedian:=FPS;
      FPSMax:=FPS;
      FPSMin:=FPS;

      with Sender do
      begin
        ListChartSourceFPSCurrent.Clear;
        ListChartSourceFPSMean.Clear;
        ListChartSourceFPSMedian.Clear;
        ListChartSourceFPSMax.Clear;
        ListChartSourceFPSMin.Clear;
      end;
    end;
    Inc(InterfaceInitialized);
  end
  else
  begin
    Inc(FrameNumber);
    FPS:=MSecsPerSec / TimeDeltaMills;
    FPSMean:=FPSMean + (FPS - FPSMean) / FrameNumber;
    if FPS > FPSMax then FPSMax:=FPS
    else if FPS < FPSMin then FPSMin:=FPS;
    FPSMedian:=(FPSMin + FPSMax) / 2;

    with Sender do
    begin
      with ListChartSourceFPSCurrent do
      begin
        if not IsUpdating then BeginUpdate;
        Add(FrameNumber, FPS);
        if Count > ChartFPSCountMax then Delete(0);
      end;
      with ListChartSourceFPSMean do
      begin
        if not IsUpdating then BeginUpdate;
        Add(FrameNumber, FPSMean);
        if Count > ChartFPSCountMax then Delete(0);
      end;
      with ListChartSourceFPSMean do
      begin
        if not IsUpdating then BeginUpdate;
        Add(FrameNumber, FPSMean);
        if Count > ChartFPSCountMax then Delete(0);
      end;
      with ListChartSourceFPSMedian do
      begin
        if not IsUpdating then BeginUpdate;
        Add(FrameNumber, FPSMedian);
        if Count > ChartFPSCountMax then Delete(0);
      end;
      with ListChartSourceFPSMax do
      begin
        if not IsUpdating then BeginUpdate;
        Add(FrameNumber, FPSMax);
        if Count > ChartFPSCountMax then Delete(0);
      end;
      with ListChartSourceFPSMin do
      begin
        if not IsUpdating then BeginUpdate;
        Add(FrameNumber, FPSMin);
        if Count > ChartFPSCountMax then Delete(0);
      end;
    end;
  end;

  Sender.ProgressBarLoading.Visible:=false;

  Sender.LabelFrameNumber.Caption:=ResStringInfoFrameNumberPrefix + IntToStr(FrameNumber);
end;
procedure OnTimer0(const Sender: TFormMain);
begin
  if InterfaceInitialized >= InterfaceInitializedThreshold then
  begin
    with Sender do
    begin
      LabelFPS.Caption:=FloatToStrF(FPS, ffNumber, 3, 2) + ResStringInfoFPSCaptionSuffix;
      LabelMSPF.Caption:=FloatToStrF(TimeDeltaMills, ffNumber, 3, 2) + ResStringInfoMSPFCaptionSuffix;

      LabelFPSCurrent.Caption:=ResStringBenchmarkFPSCurrentCaptionPrefix + FloatToStrF(FPS, ffNumber, 3, 2);
      LabelFPSMean.Caption:=ResStringBenchmarkFPSMeanCaptionPrefix + FloatToStrF(FPSMean, ffNumber, 3, 2);
      LabelFPSMedian.Caption:=ResStringBenchmarkFPSMedianCaptionPrefix + FloatToStrF(FPSMedian, ffNumber, 3, 2);
      LabelFPSMax.Caption:=ResStringBenchmarkFPSMaxCaptionPrefix + FloatToStrF(FPSMax, ffNumber, 3, 2);
      LabelFPSMin.Caption:=ResStringBenchmarkFPSMinCaptionPrefix + FloatToStrF(FPSMin, ffNumber, 3, 2);
      ListChartSourceFPSCurrent.EndUpdate;
      ListChartSourceFPSMean.EndUpdate;
      ListChartSourceFPSMedian.EndUpdate;
      ListChartSourceFPSMax.EndUpdate;
      ListChartSourceFPSMin.EndUpdate;
    end;
  end;
end;

{ Utilities }

procedure MouseKeyboardCapture(const Sender: TOpenGLControl);
begin
  SetCaptureControl(Sender);
  MouseKeyboardCaptured:=true;
  Mouse.CursorPos:=Sender.ControlToScreen(RenderControlCenter);
  {$IFNDEF Debug}
  Sender.Cursor:=crNone;
  {$ENDIF}
end;
procedure MouseKeyboardUncapture(const Sender: TOpenGLControl);
var
  Key: word;
begin
  SetCaptureControl(nil);
  MouseKeyboardCaptured:=false;
  Sender.Cursor:=crDefault;
  for Key in KeysBeingPressed do Exclude(KeysBeingPressed, Key);
end;

{$IFDEF Debug}
class function THashSetGLenumHash.Hash(const a: GLenum; const n: Longint): Longint;
begin
  exit(a and (n - 1));
end;

procedure OnDebugMessage0(Source: GLenum; Type_: GLenum; Id: GLuint; Severity: GLuint; Length: GLsizei; const Message_: PGLchar; UserParam: PGLvoid); extdecl;
// https://www.khronos.org/opengl/wiki/Debug_Output
var
  ErrorString: string = ResStringOGLErrorHeader;
  Flags: Longint = MB_ICONERROR;
  S: string;
begin
  if not (Type_ = GL_DEBUG_TYPE_ERROR) then
  begin
    if PreviousWarningTypes.Contains(Type_) then exit
    else PreviousWarningTypes.Insert(Type_);
    ErrorString:='';
    Flags:=MB_ICONWARNING;
  end;
  S:=ResStringOGLCallback + ErrorString + ' ' +
     ResStringOGLErrorSource + ' = ' + IntToStr(Source) + ', ' +
     ResStringOGLErrorType + ' = ' + IntToStr(Type_) + ', ' +
     ResStringOGLErrorId + ' = ' + IntToStr(Id) + ', ' +
     ResStringOGLErrorSeverity + ' = ' + IntToStr(Severity) + ', ' +
     ResStringOGLErrorMessage +' = ' + Message_ + ', ' +
     ResStringOGLErrorUserParam + ' = ' + IntToStr(PtrInt(UserParam));
  Application.MessageBox(PChar(S), PChar(ResStringOGLError), Flags);
end;
{$ENDIF}

initialization
  InitCriticalSection(RTLCriticalSectionLoading);

  AxisX.Init(1, 0, 0);
  AxisY.Init(0, 1, 0);
  AxisZ.Init(0, 0, 1);

  IBlockAirRenderer:=TBlockAirRenderer.Create;
  IBlockAir:=TBlockAir.Create(IBlockAirRenderer);
  IBlockAirRenderer.Block:=IBlockAir;
  IBlockOpaqueRenderer:=TBlockOpaqueRenderer.Create;
  IBlockOpaque:=TBlockOpaque.Create(IBlockOpaqueRenderer);
  IBlockOpaqueRenderer.Block:=IBlockOpaque;
  IBlockTranslucentRenderer:=TBlockTranslucentRenderer.Create;
  IBlockTranslucent:=TBlockTranslucent.Create(IBlockTranslucentRenderer);
  IBlockTranslucentRenderer.Block:=IBlockTranslucent;

  {$IFDEF Debug}
  PreviousWarningTypes:=THashSetGLenum.Create;
  {$ENDIF}

finalization
  DoneCriticalSection(RTLCriticalSectionLoading);

  ICamera.Free;
  IWorld.Free;
  IBlockAir.Destroy;
  IBlockOpaque.Destroy;
  IBlockTranslucent.Destroy;

  glDeleteProgram(ProgramShader);
  glDeleteShader(ShaderVertex3D);
  glDeleteShader(ShaderFragmentIdentity);

  {$IFDEF Debug}
  PreviousWarningTypes.Destroy;
  {$ENDIF}

end.

