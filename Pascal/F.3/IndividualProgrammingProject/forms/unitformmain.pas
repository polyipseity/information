unit UnitFormMain;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, ExtCtrls,
  OpenGLContext, LCLType, StdCtrls, ComCtrls,
  UnitGame;

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

{$R *.lfm}

{ TFormMain }

procedure TFormMain.ApplicationOnIdle(Sender: TObject; var Done: boolean);
begin
  OnIdle0(OpenGLControlRender, Done);
end;

procedure TFormMain.FormCreate(const Sender: TFormMain);
begin
  GroupBoxInfo.Caption:=ResStringInfoCaption;

  GroupBoxSettings.Caption:=ResStringSettingsCaption;
  GroupBoxWorldSize.Caption:=ResStringSettingsWorldSizeCaption;
  EditWorldSize.TextHint:=ResStringSettingsWorldSizeCaption;
  ButtonSettingsApply.Caption:=ResStringSettingsApply;

  GroupBoxBenchmark.Caption:=ResStringBenchmarkCaption;

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
  LabelFPS.Caption:=FloatToStrF(MSecsPerSec / TimeDeltaMills, ffNumber, 2, 1) + ResStringInfoFPSCaptionSuffix;
  LabelMSPF.Caption:=FloatToStrF(TimeDeltaMills, ffNumber, 2, 1) + ResStringInfoMSPFCaptionSuffix;
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

end.

