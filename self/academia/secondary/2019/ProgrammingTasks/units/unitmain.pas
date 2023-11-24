unit UnitMain;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls,
  UnitTaskA, UnitTaskB;

resourcestring
  ResStringFormCaption = 'Task Selector';
  ResStringTitleCaption = 'Task Selector';
  ResStringTaskACaption = 'Task A';
  ResStringTaskBCaption = 'Task B';

type

  { TFormMain }

  TFormMain = class(TForm)
    ButtonTaskA: TButton;
    ButtonTaskB: TButton;
    LabelTitle: TLabel;
    procedure ButtonTaskAClick(const Sender: TObject);
    procedure ButtonTaskBClick(const Sender: TObject);
    procedure FormCreate(const Sender: TObject);
  end;

var
  FormMain: TFormMain;

implementation

{$R *.lfm}

{ TFormMain }

procedure TFormMain.FormCreate(const Sender: TObject);
begin
  Caption:=ResStringFormCaption;
  LabelTitle.Caption:=ResStringTitleCaption;
  ButtonTaskA.Caption:=ResStringTaskACaption;
  ButtonTaskB.Caption:=ResStringTaskBCaption;
end;

procedure TFormMain.ButtonTaskAClick(const Sender: TObject);
begin
  Hide;
  FormTaskA.ShowModal;
  Show;
end;

procedure TFormMain.ButtonTaskBClick(const Sender: TObject);
begin
  Hide;
  FormTaskB.ShowModal;
  Show;
end;

end.

