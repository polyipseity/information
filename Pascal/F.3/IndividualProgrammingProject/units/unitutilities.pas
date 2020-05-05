unit UnitUtilities;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils;

var
  ObjectUseless: TObject;

implementation

initialization
  ObjectUseless:=TObject.Create;

finalization
  ObjectUseless.Destroy;

end.

