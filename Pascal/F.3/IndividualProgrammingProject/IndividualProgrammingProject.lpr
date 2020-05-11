program IndividualProgrammingProject;

{$mode objfpc}{$H+}

uses
  {$IFDEF UNIX}{$IFDEF UseCThreads}
  cthreads,
  {$ENDIF}{$ENDIF}
  //cmem,
  {$IFDEF Debug}
  {$DEFINE useHeapTrace}
  heaptrc,
  {$ENDIF}
  Interfaces, // this includes the LCL widgetset
  Forms, lazopenglcontext,
  UnitFormMain;

{$R *.res}

begin
  {$if declared(useHeapTrace)}
  //globalSkipIfNoLeaks:=true;
  {$endif}
  Randomize;
  RequireDerivedFormResource:=true;
  with Application do
  begin
    Scaled:=true;
    Initialize;
    CreateForm(TFormMain, FormMain);
    OnIdle:=@FormMain.ApplicationOnIdle;
    Run;
  end;
end.

