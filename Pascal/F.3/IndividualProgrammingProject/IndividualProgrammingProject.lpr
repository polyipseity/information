program IndividualProgrammingProject;

{$mode objfpc}{$H+}

uses
  {$IFDEF UNIX}{$IFDEF UseCThreads}
  cthreads,
  cmem,
  {$ENDIF}{$ENDIF}
  {$IFDEF Debug}
  {$DEFINE useHeapTrace}
  heaptrc,
  {$ENDIF}
  Interfaces, // this includes the LCL widgetset
  Forms, lazopenglcontext, UnitFormMain;

{$R *.res}

begin
  {$if declared(useHeapTrace)}
  //globalSkipIfNoLeaks:=true;
  {$endif}
  Randomize;
  RequireDerivedFormResource:=True;
  with Application do
  begin
    Scaled:=True;
    Initialize;
    CreateForm(TFormMain, FormMain);
    Run;
  end;
end.

