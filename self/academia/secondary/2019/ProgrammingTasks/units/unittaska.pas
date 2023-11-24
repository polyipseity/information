unit UnitTaskA;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls;

resourcestring
  ResStringFormCaption = 'Task A: Wealth Indicator for Face Mask';
  ResStringTitleCaption = 'Wealth Indicator for Face Mask';
  ResStringDescriptionCaption = 'Calcuate your wealth by counting how many boxes of face mask you have! Type a number below and see the result instantly.';
  ResStringEditInputTextHint = 'Number of Boxes of Face Mask';
  ResStringOutputCaptionPrefix = 'Your level of wealth is... ';
  ResStringOutputCaptionU = 'INVALID!!!';
  ResStringOutputCaption0 = 'poor.';
  ResStringOutputCaption1 = 'lower class.';
  ResStringOutputCaption2 = 'middle class.';
  ResStringOutputCaption3 = 'upper class!';
  ResStringOutputCaption4 = 'magnate!';
  ResStringBackCaption = 'Back';

type

  { TFormTaskA }

  TFormTaskA = class(TForm)
    ButtonBack: TButton;
    EditInput: TEdit;
    LabelDescription: TLabel;
    LabelOutput: TLabel;
    LabelTitle: TLabel;
    procedure ButtonBackClick(const Sender: TObject);
    procedure EditInputChange(const Sender: TEdit);
    procedure FormCreate(const Sender: TObject);
  end;

var
  FormTaskA: TFormTaskA;

implementation

{$R *.lfm}

{ TFormTaskA }

procedure TFormTaskA.EditInputChange(const Sender: TEdit);
var
  ExtendedInput: Extended;
begin
  LabelOutput.Caption:=ResStringOutputCaptionPrefix;
  if Sender.Text = '' then exit
  else
  begin
    try
      ExtendedInput:=StrToFloat(Sender.Text);
    except
      on E: EConvertError do begin
        LabelOutput.Caption:=LabelOutput.Caption + ResStringOutputCaptionU;
        exit;
      end;
    end;
  end;
  if ExtendedInput >= 30 then LabelOutput.Caption:=LabelOutput.Caption + ResStringOutputCaption4
  else if ExtendedInput >= 10 then LabelOutput.Caption:=LabelOutput.Caption + ResStringOutputCaption3
  else if ExtendedInput >= 5 then LabelOutput.Caption:=LabelOutput.Caption + ResStringOutputCaption2
  else if ExtendedInput >= 2 then LabelOutput.Caption:=LabelOutput.Caption + ResStringOutputCaption1
  else if ExtendedInput >= 0 then LabelOutput.Caption:=LabelOutput.Caption + ResStringOutputCaption0
  else LabelOutput.Caption:=LabelOutput.Caption + ResStringOutputCaptionU;
end;

procedure TFormTaskA.ButtonBackClick(const Sender: TObject);
begin
  Close;
end;

procedure TFormTaskA.FormCreate(const Sender: TObject);
begin
  Caption:=ResStringFormCaption;
  LabelTitle.Caption:=ResStringTitleCaption;
  LabelDescription.Caption:=ResStringDescriptionCaption;
  EditInput.TextHint:=ResStringEditInputTextHint;
  LabelOutput.Caption:=ResStringOutputCaptionPrefix;
  ButtonBack.Caption:=ResStringBackCaption;
end;
end.

