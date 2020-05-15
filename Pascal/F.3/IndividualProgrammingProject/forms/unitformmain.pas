unit UnitFormMain;

{$mode objfpc}{$H+}
{$IFDEF LCLCarbon}
Error: Carbon only supports Legacy OpenGL. Solution: compile to the Cocoa widgetset (Project/ProjectOptions/Additions&Overrides)
{$ENDIF}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, ExtCtrls,
  {$IFDEF Debug}{$IFDEF Windows}Windows, GLWin32WGLContext,{$ENDIF}{$ENDIF}
  OpenGLContext, LCLType, StdCtrls, ComCtrls,
  dglOpenGL,
  UnitGame;

{$R *.lfm}

resourcestring
  ResStringInfoCaption = 'Info';
  ResStringInfoFPSCaptionSuffix = 'fps';
  ResStringInfoMSPFCaptionSuffix = 'ms';
  ResStringSettingsCaption = 'Settings';
  ResStringSettingsWorldSizeCaption = 'World Size';
  ResStringSettingsApply = 'Apply';
  ResStringBenchmarkCaption = 'Benchmark';

type

  { TFormMain }

  TFormMain = class(TForm)
    ButtonSettingsApply: TButton;
    EditWorldSize: TEdit;
    GroupBoxBenchmark: TGroupBox;
    GroupBoxInfo: TGroupBox;
    GroupBoxSettings: TGroupBox;
    GroupBoxWorldSize: TGroupBox;
    LabelFPS: TLabel;
    LabelMSPF: TLabel;
    OpenGLControlRender: TOpenGLControl;
    ProgressBarLoading: TProgressBar;
    TimerSec: TTimer;
    UpDownWorldSize: TUpDown;
    procedure ApplicationOnIdle(Sender: TObject; var Done: boolean);
    procedure FormCreate(const Sender: TFormMain);

    procedure EditWorldSizeEditingDone(const Sender: TEdit);
    procedure ButtonSettingsApplyClick(const Sender: TButton);

    procedure OpenGLControlRenderResize(const Sender: TOpenGLControl);
    procedure OpenGLControlRenderDraw(const Sender: TOpenGLControl);
    procedure OpenGLControlRenderKeyDown(const Sender: TOpenGLControl; var Key: word; const Shift: TShiftState);
    procedure OpenGLControlRenderKeyUp(const Sender: TOpenGLControl; var Key: word; const Shift: TShiftState);
    procedure OpenGLControlRenderClick(const Sender: TOpenGLControl);
    procedure OpenGLControlRenderMouseMove(const Sender: TOpenGLControl; const Shift: TShiftState; const x, y: Integer);
    procedure OpenGLControlRenderExit(const Sender: TOpenGLControl);
    procedure TimerSecTimer(const Sender: TTimer);
  end;

var
  FormMain: TFormMain;

implementation

var
  WorldSize: Longint;

{ TFormMain }

procedure TFormMain.ApplicationOnIdle(Sender: TObject; var Done: boolean);
begin
  OnIdle0(OpenGLControlRender, Done);
end;

procedure TFormMain.FormCreate(const Sender: TFormMain);
{$IFDEF Debug}
{$IFDEF WINDOWS}
var
  PInfo: PWGLControlInfo;
  Attribs: array of Integer;
  WGLContextNew: HGLRC;
{$ENDIF}
{$ENDIF}
begin
  Application.OnIdle:=@ApplicationOnIdle;

  with OpenGLControlRender do
  begin
    {$IFDEF Debug}
    {$IFDEF Windows}
    // Replace with OpenGL Core
    PInfo:=GetWGLControlInfo(Handle);

    // dglOpenGL.CreateRenderingContextVersion
    wglMakeCurrent(PInfo^.DC, PInfo^.WGLContext);

    // Set attributes to describe our requested context
    SetLength(Attribs, 7);
    Attribs[0]:=WGL_CONTEXT_MAJOR_VERSION_ARB;
    Attribs[1]:=OpenGLMajorVersion;
    Attribs[2]:=WGL_CONTEXT_MINOR_VERSION_ARB;
    Attribs[3]:=OpenGLMinorVersion;
    Attribs[4]:=WGL_CONTEXT_FLAGS_ARB;
    Attribs[5]:=WGL_CONTEXT_FORWARD_COMPATIBLE_BIT_ARB;

    // Attribute flags must be finalized with a zero
    Attribs[High(Attribs)]:=0;

    // Get function pointer for new context creation function
    wglCreateContextAttribsARB:=TwglCreateContextAttribsARB(wglGetProcAddress('wglCreateContextAttribsARB'));

    if not Assigned(wglCreateContextAttribsARB) then
    begin
      raise Exception.Create('Could not get function pointer adress for wglCreateContextAttribsARB - OpenGL 3.x and above not supported!');
      wglDeleteContext(PInfo^.WGLContext);
      exit;
    end;

    // Create context
    WGLContextNew := wglCreateContextAttribsARB(PInfo^.DC, 0, @Attribs[0]);

    if WGLContextNew = 0 then
    begin
      raise Exception.Create('Could not create the desired OpenGL rendering context!');
      wglDeleteContext(WGLContextNew);
    end;

    wglDeleteContext(PInfo^.WGLContext);

    if WGLContextNew = 0 then RaiseLastOSError
    else LastPixelFormat:=0;
    // END dglOpenGL.CreateRenderingContextVersion

    PInfo^.WGLContext:=WGLContextNew;
    {$ENDIF}
    {$ENDIF}
    MakeCurrent;
  end;
  ReadExtensions;
  ReadImplementationProperties;

  GroupBoxInfo.Caption:=ResStringInfoCaption;

  GroupBoxSettings.Caption:=ResStringSettingsCaption;
  GroupBoxWorldSize.Caption:=ResStringSettingsWorldSizeCaption;
  EditWorldSize.TextHint:=ResStringSettingsWorldSizeCaption;
  ButtonSettingsApply.Caption:=ResStringSettingsApply;

  GroupBoxBenchmark.Caption:=ResStringBenchmarkCaption;

  OnCreate0(Sender);

  WorldSize:=StrToInt(EditWorldSize.Text);
  Apply1(OpenGLControlRender, WorldSize, ProgressBarLoading);
end;
procedure TFormMain.EditWorldSizeEditingDone(const Sender: TEdit);
begin
  if Sender.Text = '' then Sender.Text:=IntToStr(WorldSize)
  else WorldSize:=StrToInt(Sender.Text);
end;

procedure TFormMain.ButtonSettingsApplyClick(const Sender: TButton);
begin
  Apply1(OpenGLControlRender, WorldSize, ProgressBarLoading);
end;

procedure TFormMain.TimerSecTimer(const Sender: TTimer);
begin
  LabelFPS.Caption:=FloatToStrF(MSecsPerSec / TimeDeltaMills, ffNumber, 1, 1) + ResStringInfoFPSCaptionSuffix;
  LabelMSPF.Caption:=FloatToStrF(TimeDeltaMills, ffNumber, 1, 1) + ResStringInfoMSPFCaptionSuffix;
end;

procedure TFormMain.OpenGLControlRenderResize(const Sender: TOpenGLControl);
begin
  OnResize0(Sender);
end;
procedure TFormMain.OpenGLControlRenderDraw(const Sender: TOpenGLControl);
begin
  Draw0(Sender);
end;
procedure TFormMain.OpenGLControlRenderKeyDown(const Sender: TOpenGLControl; var Key: word; const Shift: TShiftState);
begin
  KeyDown0(Sender, Key, Shift);
end;
procedure TFormMain.OpenGLControlRenderKeyUp(const Sender: TOpenGLControl; var Key: word; const Shift: TShiftState);
begin
  KeyUp0(Sender, Key, Shift);
end;
procedure TFormMain.OpenGLControlRenderMouseMove(const Sender: TOpenGLControl; const Shift: TShiftState; const x, y: Integer);
begin
  OnMouseMove0(Sender, Shift, x, y);
end;
procedure TFormMain.OpenGLControlRenderClick(const Sender: TOpenGLControl);
begin
  OnClick0(Sender);
  Sender.SetFocus;
end;
procedure TFormMain.OpenGLControlRenderExit(const Sender: TOpenGLControl);
begin
  OnExit0(Sender);
end;

initialization
  InitOpenGL;

end.

