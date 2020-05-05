unit UnitWorld;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils,
  OpenGLContext, GHashMap,
  gl;

resourcestring
  ResStringEUnexpected = 'Unexpected';
  ResStringEIllegal = 'Illegal';

type
  TGLBox = TOpenGLControl;

  TEnumFacing = (Up, Down, North, East, South, West);
  TSetEnumFacing = set of TEnumFacing;
  TWorldDataRange = 0..63;

  { World: Forward }
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
  TPositionI = specialize TGPosition<Integer>;
  TPositionGLd = specialize TGPosition<GLdouble>;
  TBlock = class;
  TWorld = class;
  TBlockAir = class;
  TBlockExist = class;
  TBlockOpaque = class;
  TBlockTranslucent = class;
  TArrayPosition = array of TPositionI;

  { Renderer: Forward }
  TCamera = class;
  TBlockRenderer = class;
  TBlockRendererDefault = class;
  TWorldRenderer = class;
  THashMapVisibleHash = class;
  THashMapVisibleValue = record
    Key: TPositionI;
    Value: TSetEnumFacing;
  end;
  THashMapVisible = specialize THashMap<TPositionI, THashMapVisibleValue, THashMapVisibleHash>;
  TArraySixteenGLd = array[0..15] of GLdouble;
  TArrayFourGLi = array[0..3] of GLint;

  { World }

  TBlock = class
    private
      FRenderer: TBlockRenderer;
    public
      constructor Create(const Renderer: TBlockRenderer = nil);
      procedure SetRenderer(const Renderer: TBlockRenderer);
      property Renderer: TBlockRenderer read FRenderer write SetRenderer;
      function IsAir: Boolean; virtual; abstract;
      function IsOpaque: Boolean; virtual; abstract;
      destructor Destroy; override;
  end;
  TBlockAir = class(TBlock)
    function IsAir: Boolean; override;
    function IsOpaque: Boolean; override;
  end;
  TBlockExist = class(TBlock)
    function IsAir: Boolean; override;
  end;
  TBlockOpaque = class(TBlockExist)
    function IsOpaque: Boolean; override;
  end;
  TBlockTranslucent = class(TBlockExist)
    function IsOpaque: Boolean; override;
  end;

  TFunctionWorldForeachBlock = function(Block: TBlock; Position: TPositionI; Arg: Pointer): TBlock;
  TFunctionWorldForeachBlockOfObject = function(Block: TBlock; Position: TPositionI; Arg: Pointer): TBlock of object;
  TFunctionBlockForeachNeighbor = function(BlockTo, BlockFrom: TBlock; PositionTo, PositionFrom: TPositionI; Facing: TEnumFacing; Arg: Pointer): TBlock;
  TFunctionBlockForeachNeighborOfObject = function(BlockTo, BlockFrom: TBlock; PositionTo, PositionFrom: TPositionI; Facing: TEnumFacing; Arg: Pointer): TBlock of object;
  TWorld = class
    private
      FRenderer: TWorldRenderer;
    public
      constructor Create(const Renderer: TWorldRenderer = nil);
      procedure SetRenderer(const Renderer: TWorldRenderer);
      property Renderer: TWorldRenderer read FRenderer write SetRenderer;
      function GetBlock(const Position: TPositionI): TBlock; virtual;
      procedure SetBlock(const Position: TPositionI; const Block: TBlock); virtual;
      procedure ForeachBlock(const f: TFunctionWorldForeachBlock; const Arg: Pointer = nil); virtual; overload;
      procedure ForeachBlock(const f: TFunctionWorldForeachBlockOfObject; const Arg: Pointer = nil); virtual; overload;
      procedure ForeachNeighbor(const Position: TPositionI; const f: TFunctionBlockForeachNeighbor; const Arg: Pointer = nil); overload;
      procedure ForeachNeighbor(const Position: TPositionI; const f: TFunctionBlockForeachNeighborOfObject; const Arg: Pointer = nil); overload;
    private
      Data: array[TWorldDataRange, TWorldDataRange, TWorldDataRange] of TBlock;
      function InitializeData(Block: TBlock; Position: TPositionI; Arg: Pointer): TBlock;
    public
      destructor Destroy; override;
  end;

  { Renderer }
  TCamera = class
    public
      FOV: GLdouble;
      zNear: GLdouble;
      zFar: GLdouble;
      Position: TPositionGLd;
      constructor Create;
      procedure Render(const Sender: TGLBox);
    public
      destructor Destroy; override;
  end;

  TBlockRenderer = class
    private
      FBlock: TBlock;
    public
      constructor Create(const Block: TBlock = nil);
      procedure SetBlock(const Block: TBlock);
      property Block: TBlock read FBlock write SetBlock;
      procedure Render(const Position: TPositionI; const Facings: TSetEnumFacing); virtual; abstract;
      destructor Destroy; override;
  end;
  TBlockRendererDefault = class(TBlockRenderer)
    public
      procedure Render(const Position: TPositionI; const Facings: TSetEnumFacing); override;
      procedure RenderUp(const Position: TPositionI); virtual;
      procedure RenderDown(const Position: TPositionI); virtual;
      procedure RenderNorth(const Position: TPositionI); virtual;
      procedure RenderEast(const Position: TPositionI); virtual;
      procedure RenderSouth(const Position: TPositionI); virtual;
      procedure RenderWest(const Position: TPositionI); virtual;
  end;

  TWorldRenderer = class
    private
      FWorld: TWorld;
      Visible: THashMapVisible;
      function InitializeVisible(Block: TBlock; Position: TPositionI; Arg: Pointer): TBlock;
      function CheckNeighborBlockForVisible(BlockTo, BlockFrom: TBlock; PositionTo, PositionFrom: TPositionI; Facing: TEnumFacing; Arg: Pointer): TBlock;
    public
      constructor Create(const World: TWorld = nil);
      procedure SetWorld(const World: TWorld);
      property World: TWorld read FWorld write SetWorld;
      procedure Render;
      destructor Destroy; override;
  end;

  THashMapVisibleHash = class
    public
      class function Hash(const a: TPositionI; const n: longint): longint;
      class function Equal(const AKey1, AKey2: TPositionI): Boolean;
  end;

{ World }

{ Renderer }
procedure Draw0(const Sender: TGLBox);

const
  SetWorldDataRange = [Low(TWorldDataRange)..High(TWorldDataRange)];

implementation
uses
  { World }
  { Renderer } glu;

var
  ICamera: TCamera;
  IWorld: TWorld;
  IWorldRenderer: TWorldRenderer;
  IBlockAir: TBlock;
  IBlockAirRenderer: TBlockRenderer;
  IBlockOpaque: TBlock;
  IBlockOpaqueRenderer: TBlockRenderer;
  IBlockTranslucent: TBlock;
  IBlockTranslucentRenderer: TBlockRenderer;

{ World }

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
    TEnumFacing.Up: exit(Up);
    TEnumFacing.Down: exit(Down);
    TEnumFacing.North: exit(North);
    TEnumFacing.East: exit(East);
    TEnumFacing.South: exit(South);
    TEnumFacing.West: exit(West);
    else raise EAbort(ResStringEUnexpected);
  end;
end;
function TGPosition.Up: TGPosition;
begin
  exit(TGPosition.Create(x, y + 1, z));
end;
function TGPosition.Down: TGPosition;
begin
  exit(TGPosition.Create(x, y - 1, z));
end;
function TGPosition.North: TGPosition;
begin
  exit(TGPosition.Create(x, y, z + 1));
end;
function TGPosition.East: TGPosition;
begin
  exit(TGPosition.Create(x + 1, y, z));
end;
function TGPosition.South: TGPosition;
begin
  exit(TGPosition.Create(x, y, z - 1));
end;
function TGPosition.West: TGPosition;
begin
  exit(TGPosition.Create(x - 1, y, z));
end;

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

function TBlockAir.IsAir: Boolean;
begin
  exit(true);
end;
function TBlockAir.IsOpaque: Boolean;
begin
  exit(false);
end;

function TBlockExist.IsAir: Boolean;
begin
  exit(false);
end;

function TBlockOpaque.IsOpaque: Boolean;
begin
  exit(true);
end;

function TBlockTranslucent.IsOpaque: Boolean;
begin
  exit(false);
end;

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
function TWorld.InitializeData(Block: TBlock; Position: TPositionI; Arg: Pointer): TBlock;
begin
  case Random(3) of
    0: exit(IBlockAir);
    1: exit(IBlockOpaque);
    2: exit(IBlockTranslucent);
    else raise EAbort.Create(ResStringEUnexpected);
  end;
end;
function TWorld.GetBlock(const Position: TPositionI): TBlock;
begin
  if (Position.x in SetWorldDataRange) and (Position.y in SetWorldDataRange) and (Position.z in SetWorldDataRange) then
  begin
    exit(Data[Position.x][Position.z][Position.y]);
  end
  else exit(nil);
end;
procedure TWorld.SetBlock(const Position: TPositionI; const Block: TBlock);
begin
  if Block = nil then exit();
  if (Position.x in SetWorldDataRange) and (Position.y in SetWorldDataRange) and (Position.z in SetWorldDataRange) then
  begin
    Data[Position.x][Position.z][Position.y]:=Block;
  end;
end;
procedure TWorld.ForeachBlock(const f: TFunctionWorldForeachBlock; const Arg: Pointer = nil);
var
  x, y, z: TWorldDataRange;
  Position: TPositionI;
begin
  for x in SetWorldDataRange do
  begin
    for z in SetWorldDataRange do
    begin
      for y in SetWorldDataRange do
      begin
        Position:=TPositionI.Create(x, y, z);
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
  Position: TPositionI;
begin
  for x in SetWorldDataRange do
  begin
    for z in SetWorldDataRange do
    begin
      for y in SetWorldDataRange do
      begin
        Position:=TPositionI.Create(x, y, z);
        try
          SetBlock(Position, f(GetBlock(Position), Position, Arg));
        finally
          Position.Destroy;
        end;
      end;
    end;
  end;
end;
procedure TWorld.ForeachNeighbor(const Position: TPositionI; const f: TFunctionBlockForeachNeighbor; const Arg: Pointer = nil);
var
  BlockFrom: TBlock;
  Facing: TEnumFacing;
  PositionTo: TPositionI;
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
procedure TWorld.ForeachNeighbor(const Position: TPositionI; const f: TFunctionBlockForeachNeighborOfObject; const Arg: Pointer = nil);
var
  BlockFrom: TBlock;
  Facing: TEnumFacing;
  PositionTo: TPositionI;
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

constructor TCamera.Create;
begin
  FOV:=60;
  zNear:=1;
  zFar:=16;
  Position:=TPositionGLd.Create(-5, 10, 0);
end;
procedure TCamera.Render(const Sender: TGLBox);
begin
  glMatrixMode(GL_PROJECTION);
  glLoadIdentity;
  gluPerspective(FOV, Sender.Width / Sender.Height, zNear, zFar);
  glMatrixMode(GL_MODELVIEW);
  glTranslated(-Position.x, -Position.y, -Position.z);
end;
destructor TCamera.Destroy;
begin
  try
    Position.Destroy;
  finally
    inherited;
  end;
end;

constructor TBlockRenderer.Create(const Block: TBlock);
begin
  Self.Block:=Block;
end;
procedure TBlockRenderer.SetBlock(const Block: TBlock);
begin
  if (Self.Block <> nil) and (Block <> nil) then raise EAbort.Create(ResStringEIllegal);
  FBlock:=Block;
end;
procedure TBlockRendererDefault.Render(const Position: TPositionI; const Facings: TSetEnumFacing);
begin
  if Up in Facings then RenderUp(Position);
  if Down in Facings then RenderDown(Position);
  if North in Facings then RenderNorth(Position);
  if East in Facings then RenderEast(Position);
  if South in Facings then RenderSouth(Position);
  if West in Facings then RenderWest(Position);
end;
procedure TBlockRendererDefault.RenderUp(const Position: TPositionI);
var
  Model, Proj: TArraySixteenGLd;
  View: TArrayFourGLi;
  WinX, WinY, WinZ: GLdouble;
begin
  glGetDoublev(GL_MODELVIEW_MATRIX, @Model);
  glGetDoublev(GL_PROJECTION_MATRIX, @Proj);
  glGetIntegerv(GL_VIEWPORT, @View);
  glColor3f(Random, Random, Random);
  glBegin(GL_QUADS);
  with Position do
  begin
    gluProject(x, y + 1, z, @Model, @Proj, @View, @WinX, @WinY, @WinZ);
    glVertex3d(WinX, WinY, WinZ);
    gluProject(x + 1, y + 1, z, @Model, @Proj, @View, @WinX, @WinY, @WinZ);
    glVertex3d(WinX, WinY, WinZ);
    gluProject(x + 1, y + 1, z + 1, @Model, @Proj, @View, @WinX, @WinY, @WinZ);
    glVertex3d(WinX, WinY, WinZ);
    gluProject(x, y + 1, z + 1, @Model, @Proj, @View, @WinX, @WinY, @WinZ);
    glVertex3d(WinX, WinY, WinZ);
  end;
  glEnd;
end;
procedure TBlockRendererDefault.RenderDown(const Position: TPositionI);    
begin
end;
procedure TBlockRendererDefault.RenderNorth(const Position: TPositionI);
begin
end;
procedure TBlockRendererDefault.RenderEast(const Position: TPositionI);
begin
end;
procedure TBlockRendererDefault.RenderSouth(const Position: TPositionI);
begin
end;
procedure TBlockRendererDefault.RenderWest(const Position: TPositionI);
begin
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

constructor TWorldRenderer.Create(const World: TWorld = nil);
begin
  Visible:=THashMapVisible.Create;
  Self.World:=World;
end;
procedure TWorldRenderer.SetWorld(const World: TWorld);
begin
  if (Self.World <> nil) and (World <> nil) then raise EAbort.Create(ResStringEIllegal);
  FWorld:=World;
  if Self.World <> nil then Self.World.ForeachBlock(@InitializeVisible);
end;
function TWorldRenderer.InitializeVisible(Block: TBlock; Position: TPositionI; Arg: Pointer): TBlock;
begin
  World.ForeachNeighbor(Position, @CheckNeighborBlockForVisible);
  exit(Block);
end;
function TWorldRenderer.CheckNeighborBlockForVisible(BlockTo, BlockFrom: TBlock; PositionTo, PositionFrom: TPositionI; Facing: TEnumFacing; Arg: Pointer): TBlock;
var
  Value: THashMapVisibleValue;
  Facings: TSetEnumFacing;
begin
  if BlockTo = nil then exit(BlockFrom);
  if not BlockTo.IsOpaque then
  begin
    if not Visible.Contains(PositionFrom) then
    begin
      with Value do
      begin
        Key:=PositionFrom.Clone;
        Value:=[];
      end;
    end
    else Value:=Visible[PositionFrom];
    Facings:=Value.Value;
    Include(Facings, Facing);
    Value.Value:=Facings;
    Visible[Value.Key]:=Value;
  end;
  exit(BlockFrom);
end;
procedure TWorldRenderer.Render;
var
  Iterator: THashMapVisible.TIterator;
begin
  if not Visible.IsEmpty then
  begin
    Iterator:=Visible.Iterator;
    repeat
      World.GetBlock(Iterator.Key).Renderer.Render(Iterator.Key, Iterator.Value.Value);
    until not Iterator.Next;
    Iterator.Destroy;
  end;
end;
destructor TWorldRenderer.Destroy;
var
  Iterator: THashMapVisible.TIterator;
  Keys: TArrayPosition;
  i: Integer = 0;
begin
  try
    if not Visible.IsEmpty then
    begin
      Iterator:=Visible.Iterator;
      SetLength(Keys, Visible.Size);
      repeat
        Keys[i]:=Iterator.Key;
        inc(i);
      until not Iterator.Next;
      for i:=i-1 downto 0 do Keys[i].Destroy; // Do NOT use a for-in loop.
      Iterator.Destroy;
    end;
    Visible.Destroy;
    if World <> nil then
    begin
      World.Renderer:=nil;
      World.Destroy;
    end;
  finally
    inherited;
  end;
end;

class function THashMapVisibleHash.Hash(const a: TPositionI; const n: longint): longint;
var
  h: longword = 5381;
  e: integer;
begin
  with a do
  begin
    for e in [x, y, z] do h:=((h shl 5) xor (h shr 27)) xor e;
  end;
  exit(h and (n - 1));
end;
class function THashMapVisibleHash.Equal(const AKey1, AKey2: TPositionI): Boolean;
begin
  exit(AKey1 = AKey2);
end;

procedure Draw0(const Sender: TGLBox);
begin
  glClearColor(0.52, 0.80, 0.92, 1.0); // Sky
  glClear(GL_COLOR_BUFFER_BIT or GL_DEPTH_BUFFER_BIT);
  glLoadIdentity;
  ICamera.Render(Sender);
  IWorldRenderer.Render;
  Sender.SwapBuffers;
end;

initialization
  IBlockAirRenderer:=TBlockRendererDefault.Create;
  IBlockAir:=TBlockAir.Create(IBlockAirRenderer);
  IBlockAirRenderer.Block:=IBlockAir;
  IBlockOpaqueRenderer:=TBlockRendererDefault.Create;
  IBlockOpaque:=TBlockOpaque.Create(IBlockOpaqueRenderer);
  IBlockOpaqueRenderer.Block:=IBlockOpaque;
  IBlockTranslucentRenderer:=TBlockRendererDefault.Create;
  IBlockTranslucent:=TBlockTranslucent.Create(IBlockTranslucentRenderer);
  IBlockTranslucentRenderer.Block:=IBlockTranslucent;

  IWorldRenderer:=TWorldRenderer.Create;
  IWorld:=TWorld.Create(IWorldRenderer);
  IWorldRenderer.World:=IWorld;

  ICamera:=TCamera.Create;

finalization
  ICamera.Destroy;
  IWorld.Destroy;
  IBlockAir.Destroy;
  IBlockOpaque.Destroy;
  IBlockTranslucent.Destroy;

end.

