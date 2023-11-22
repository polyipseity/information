unit UnitTaskB;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, ExtCtrls, StdCtrls,
  LCLType, math, typinfo;

resourcestring
  ResStringFormCaption = 'Task B: Custom';
  ResStringTitleCaption = 'SUVAT Equations Calculator';
  ResStringDisplacementCaption = 'displacement (s/m)';
  ResStringInitialVelocityCaption = 'initial velocity (u/m/s)';
  ResStringFinalVelocityCaption = 'final velocity (v/m/s)';
  ResStringAccelerationCaption = 'acceleration (a/m/s^2)';
  ResStringTimeCaption = 'time (t/s)';
  ResStringCalculateCaption = 'Calculate';
  ResStringResetCaption = 'Reset';
  ResStringDescriptionCaption = 'Input 3 of the variables and click "Calculate" to calculate the 2 unknowns.';
  ResStringBackCaption = 'Back';
  ResStringInvalidText = 'invalid'; { sqrt(-1) }
  ResStringOverflowText = 'overflow';
  ResStringUnderflowText = 'underflow';
  ResStringZeroDivideText = 'divide by 0'; { 1 / 0 }

type

  { TEquation }

  TRangeArrayEnumVariableKnown = 0..2;
  TRangeArrayEnumVariableUnknown = 0..1;
  TEnumVariable = (Displacement, Velocity0, Velocity, Acceleration, Time);
  TArrayEnumVariableKnown = array[TRangeArrayEnumVariableKnown] of TEnumVariable;
  TFunctionEquationResults = array of Extended;
  TFunctionEquation = function(const Subject: TEnumVariable; const a, b, c: Extended): TFunctionEquationResults;
  TEquation = class
  public
    class var
      EquationS: TEquation;
      EquationU: TEquation;
      EquationV: TEquation;
      EquationA: TEquation;
      EquationT: TEquation;
    constructor Create(const FunctionEquation: TFunctionEquation);
    function Compute(const Subject: TEnumVariable; const a, b, c: Extended): TFunctionEquationResults;
    class function FindEquation(const Subject: TEnumVariable; const Known: TArrayEnumVariableKnown): TEquation;
  private
    FunctionEquation: TFunctionEquation;
    class constructor Initialize;
  end;

  { TFormTaskB }

  ArrayTLabeledEdit = array of TLabeledEdit;
  TFormTaskB = class(TForm)
    ButtonBack: TButton;
    ButtonCalculate: TButton;
    ButtonReset: TButton;
    LabelDescription: TLabel;
    LabeledEditDisplacement: TLabeledEdit;
    LabeledEditInitialVelocity: TLabeledEdit;
    LabeledEditFinalVelocity: TLabeledEdit;
    LabeledEditAcceleration: TLabeledEdit;
    LabeledEditTime: TLabeledEdit;
    LabelTitle: TLabel;
    procedure ButtonBackClick(const Sender: TObject);
    procedure ButtonCalculateClick(const Sender: TButton);
    procedure ButtonResetClick(const Sender: TObject);
    procedure FormCreate(const Sender: TObject);
    procedure LabeledEditVariableChange(const Sender: TLabeledEdit);
  private
    ArrayLabeledEdit: ArrayTLabeledEdit;
    procedure MarkValid(const Valid: Boolean);
  public

  end;

  { TArrayUtils<T> }
  { https://stackoverflow.com/a/53550340/9341868 }
  generic TArrayUtils<T> = class
  public
    class function Contains(const x: T; const a: array of T): boolean;
  end;

  TArrayUtilsEnumVariable = specialize TArrayUtils<TEnumVariable>;

var
  FormTaskB: TFormTaskB;

function StrToFloatSafe(const s: String; var r: Extended): Boolean;

implementation

{$R *.lfm}

{ TFormTaskB }

procedure TFormTaskB.FormCreate(const Sender: TObject);
begin
  { Order is Displacement (s), initial Velocity (u), final Velocity (v), Acceleration (a), Time (t). }
  ArrayLabeledEdit:=ArrayTLabeledEdit.create(LabeledEditDisplacement, LabeledEditInitialVelocity, LabeledEditFinalVelocity, LabeledEditAcceleration, LabeledEditTime);

  Caption:=ResStringFormCaption;
  LabelTitle.Caption:=ResStringTitleCaption;
  LabeledEditDisplacement.TextHint:=ResStringDisplacementCaption;
  LabeledEditDisplacement.EditLabel.Caption:=ResStringDisplacementCaption;
  LabeledEditInitialVelocity.TextHint:=ResStringInitialVelocityCaption;
  LabeledEditInitialVelocity.EditLabel.Caption:=ResStringInitialVelocityCaption;
  LabeledEditFinalVelocity.TextHint:=ResStringFinalVelocityCaption;
  LabeledEditFinalVelocity.EditLabel.Caption:=ResStringFinalVelocityCaption;
  LabeledEditAcceleration.TextHint:=ResStringAccelerationCaption;
  LabeledEditAcceleration.EditLabel.Caption:=ResStringAccelerationCaption;
  LabeledEditTime.TextHint:=ResStringTimeCaption;
  LabeledEditTime.EditLabel.Caption:=ResStringTimeCaption;
  LabelDescription.Caption:=ResStringDescriptionCaption;
  ButtonCalculate.Caption:=ResStringCalculateCaption;
  ButtonReset.Caption:=ResStringResetCaption;
  ButtonBack.Caption:=ResStringBackCaption;
end;

procedure TFormTaskB.LabeledEditVariableChange(const Sender: TLabeledEdit);
var
  ExtendedUnused: Extended = 0;
  LabeledEdit: TLabeledEdit;
  IntegerEmptyEdits: Integer = 0;
begin
  if (Sender.Text = '') or StrToFloatSafe(Sender.Text, ExtendedUnused) then
  begin
    Sender.Color:=clDefault;

    for LabeledEdit in ArrayLabeledEdit do
    begin
      if LabeledEdit.Color <> clDefault then
      begin
        MarkValid(false);
        exit;
      end
      else if LabeledEdit.Text = '' then inc(IntegerEmptyEdits);
    end;
    MarkValid(IntegerEmptyEdits = High(TRangeArrayEnumVariableUnknown) + 1);
  end
  else
  begin
    Sender.Color:=$008080FF;
    MarkValid(false);
  end;
end;

procedure TFormTaskB.ButtonBackClick(const Sender: TObject);
begin
  Close;
end;

procedure TFormTaskB.ButtonCalculateClick(const Sender: TButton);
var
  LabeledEdit: TLabeledEdit;
  i: Integer = Low(ArrayLabeledEdit);
  ArrayEnumVariableKnown: TArrayEnumVariableKnown;
  ArrayVariableKnown: array[TRangeArrayEnumVariableKnown] of Extended;
  k: Integer = Low(TRangeArrayEnumVariableKnown);
  ArrayEnumVariableUnknown: array[TRangeArrayEnumVariableUnknown] of TEnumVariable;
  u: Integer = Low(TRangeArrayEnumVariableUnknown);
  EnumVariableUnknown: TEnumVariable;
  FunctionEquationResult: Extended;
begin
  for LabeledEdit in ArrayLabeledEdit do
  begin
    LabeledEdit.ReadOnly:=true;
    if LabeledEdit.Text <> '' then
    begin
      ArrayEnumVariableKnown[k]:=TEnumVariable(i);
      ArrayVariableKnown[k]:=StrToFloat(LabeledEdit.Text);
      inc(k);
    end
    else
    begin
      ArrayEnumVariableUnknown[u]:=TEnumVariable(i);
      inc(u);
    end;
    inc(i);
  end;
  for EnumVariableUnknown in ArrayEnumVariableUnknown do
  begin
    try
      for FunctionEquationResult in TEquation.FindEquation(EnumVariableUnknown, ArrayEnumVariableKnown).Compute(EnumVariableUnknown, ArrayVariableKnown[Low(TRangeArrayEnumVariableKnown)], ArrayVariableKnown[Low(TRangeArrayEnumVariableKnown) + 1], ArrayVariableKnown[Low(TRangeArrayEnumVariableKnown) + 2]) do
      begin
        if ArrayLabeledEdit[Ord(EnumVariableUnknown)].Text <> '' then ArrayLabeledEdit[Ord(EnumVariableUnknown)].Text:=ArrayLabeledEdit[Ord(EnumVariableUnknown)].Text + ' or ';
        ArrayLabeledEdit[Ord(EnumVariableUnknown)].Text:=ArrayLabeledEdit[Ord(EnumVariableUnknown)].Text + FloatToStr(FunctionEquationResult);
      end;
      ArrayLabeledEdit[Ord(EnumVariableUnknown)].Color:=clDefault;
    except
      on EInvalidOp do ArrayLabeledEdit[Ord(EnumVariableUnknown)].Text:=ResStringInvalidText;
      on EOverflow do ArrayLabeledEdit[Ord(EnumVariableUnknown)].Text:=ResStringOverflowText;
      on EUnderflow do ArrayLabeledEdit[Ord(EnumVariableUnknown)].Text:=ResStringUnderflowText;
      on EZeroDivide do ArrayLabeledEdit[Ord(EnumVariableUnknown)].Text:=ResStringZeroDivideText;
    end;
  end;
  MarkValid(false);
end;

procedure TFormTaskB.ButtonResetClick(const Sender: TObject);
var
  LabeledEdit: TLabeledEdit;
begin
  for LabeledEdit in ArrayLabeledEdit do
  begin
    LabeledEdit.Text:='';
    LabeledEdit.ReadOnly:=false;
  end;
end;


procedure TFormTaskB.MarkValid(const Valid: Boolean);
var
  LabeledEdit: TLabeledEdit;
begin
  ButtonCalculate.Enabled:=Valid;
  if Valid then
  begin
    for LabeledEdit in ArrayLabeledEdit do if LabeledEdit.Text = '' then LabeledEdit.Enabled:=false;
  end
  else for LabeledEdit in ArrayLabeledEdit do LabeledEdit.Enabled:=true;
end;

{ Utilities }

function StrToFloatSafe(const s: String; var r: Extended): Boolean;
begin
  try
    r:=StrToFloat(s);
  except
    on E: EConvertError do exit(false);
  end;
  exit(true);
end;

{ TArrayUtils<T> }
{ https://stackoverflow.com/a/53550340/9341868 }
class function TArrayUtils.Contains(const x: T; const a: array of T): boolean;
var
  y: T;
begin
  for y in a do if x = y then exit(true);
  exit(false);
end;

{ TEquation }

class function TEquation.FindEquation(const Subject: TEnumVariable; const Known: TArrayEnumVariableKnown): TEquation;
begin
  if not ((Subject = Displacement) or (TArrayUtilsEnumVariable.Contains(Displacement, Known))) then exit(EquationS)
  else if not ((Subject = Velocity0) or (TArrayUtilsEnumVariable.Contains(Velocity0, Known))) then exit(EquationU)
  else if not ((Subject = Velocity) or (TArrayUtilsEnumVariable.Contains(Velocity, Known))) then exit(EquationV)
  else if not ((Subject = Acceleration) or (TArrayUtilsEnumVariable.Contains(Acceleration, Known))) then exit(EquationA)
  else if not ((Subject = Time) or (TArrayUtilsEnumVariable.Contains(Time, Known))) then exit(EquationT)
  else raise Exception.Create('Illegal arguments.');
end;

function TEquation.Compute(const Subject: TEnumVariable; const a, b, c: Extended): TFunctionEquationResults;
begin
  exit(FunctionEquation(Subject, a, b, c));
end;

constructor TEquation.Create(const FunctionEquation: TFunctionEquation);
begin
  Self.FunctionEquation:=FunctionEquation;
end;

{ Order is Displacement (s), initial Velocity (u), final Velocity (v), Acceleration (a), Time (t). }
{ v = u + at }
function EquationSFunction(const Subject: TEnumVariable; const a, b, c: Extended): TFunctionEquationResults;
begin
  case Subject of
  Velocity: exit(TFunctionEquationResults.Create(a + b * c)); { a: u; b: a; c: t }
  Velocity0: exit(TFunctionEquationResults.Create(a - b * c)); { a: v; b: a; c: t }
  Acceleration: exit(TFunctionEquationResults.Create((b - a) / c)); { a: u; b: v; c: t }
  Time: exit(TFunctionEquationResults.Create((b - a) / c)); { a: u; b: v; c: a }
  else raise Exception.Create('Illegal arguments.');
  end;
end;

{ s = ut + 1/2(at ^ 2) }
function EquationVFunction(const Subject: TEnumVariable; const a, b, c: Extended): TFunctionEquationResults;
var
  t: Extended;
begin
  case Subject of
  Displacement: exit(TFunctionEquationResults.Create(a * c + b * c ** 2 / 2)); { a: u; b: a; c: t }
  Velocity0: exit(TFunctionEquationResults.Create(a / c - b * c / 2)); { a: s; b: a; c: t }
  Time: { a: s; b: u; c: a }
  begin
    if c <> 0 then exit(TFunctionEquationResults.Create((-sqrt(2 * c * a + b ** 2) - b) / c, (sqrt(2 * c * a + b ** 2) - b) / c))
    else
    begin
      t:=a / b;
      if t >= 0 then exit(TFunctionEquationResults.Create(t, NegInfinity))
      else exit(TFunctionEquationResults.Create(t, Infinity));
    end;
  end;
  Acceleration: exit(TFunctionEquationResults.Create(2 * (a - c * b) / c ** 2)); { a: s; b: u; c: t }
  else raise Exception.Create('Illegal arguments.');
  end;
end;

{ s = 1/2(u + v)t }
function EquationAFunction(const Subject: TEnumVariable; const a, b, c: Extended): TFunctionEquationResults;
begin
  case Subject of
  Displacement: exit(TFunctionEquationResults.Create((a + b) * c / 2)); { a: u; b: v; c: t }
  Velocity0: exit(TFunctionEquationResults.Create(2 * a / c - b)); { a: s; b: v; c: t }
  Velocity: exit(TFunctionEquationResults.Create(2 * a / c - b)); { a: s; b: u; c: t }
  Time: exit(TFunctionEquationResults.Create(2 * a / (b + c))); { a: s; b: u; c: v }
  else raise Exception.Create('Illegal arguments.');
  end;
end;

{ v ^ 2 = u ^ 2 + 2as }
function EquationTFunction(const Subject: TEnumVariable; const a, b, c: Extended): TFunctionEquationResults;
begin
  case Subject of
  Velocity: exit(TFunctionEquationResults.Create(-sqrt(2 * c * a + b ** 2), sqrt(2 * c * a + b ** 2))); { a: s; b: u; c: a }
  Velocity0: exit(TFunctionEquationResults.Create(-sqrt(b ** 2 - 2 * c * a), sqrt(b ** 2 - 2 * c * a))); { a: s; b: v; c: a }
  Acceleration: exit(TFunctionEquationResults.Create((c ** 2 - b ** 2) / (2 * a))); { a: s; b: u; c: v }
  Displacement: exit(TFunctionEquationResults.Create((b ** 2 - a ** 2) / (2 * c))); { a: u; b: v; c: a }
  else raise Exception.Create('Illegal arguments.');
  end;
end;

{ s = vt - 1/2(at ^ 2) }
function EquationUFunction(const Subject: TEnumVariable; const a, b, c: Extended): TFunctionEquationResults;
var
  t: Extended;
begin
  case Subject of
  Displacement: exit(TFunctionEquationResults.Create(a * c - b * c ** 2 / 2)); { a: v; b: a; c: t }
  Velocity: exit(TFunctionEquationResults.Create(b * c / 2 + a / c)); { a: s; b: a; c: t }
  Time: { a: s; b: v; c: a }
  begin
    if c <> 0 then exit(TFunctionEquationResults.Create(-sqrt(b ** 2 - 2 * c * a) + b / c, sqrt(b ** 2 - 2 * c * a) + b / c))
    else
    begin
      t:=a / b;
      if t >= 0 then exit(TFunctionEquationResults.Create(t, NegInfinity))
      else exit(TFunctionEquationResults.Create(t, Infinity));
    end;
  end;
  Acceleration: exit(TFunctionEquationResults.Create(-(2 * (a - c * b) / c ** 2))); { a: s; b: v; c: t }
  else raise Exception.Create('Illegal arguments.');
  end;
end;

class constructor TEquation.Initialize;
begin
  EquationS:=TEquation.Create(@EquationSFunction);
  EquationU:=TEquation.Create(@EquationUFunction);
  EquationV:=TEquation.Create(@EquationVFunction);
  EquationA:=TEquation.Create(@EquationAFunction);
  EquationT:=TEquation.Create(@EquationTFunction);
end;

end.

